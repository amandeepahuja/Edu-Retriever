# services/faiss_index.py

import faiss
import numpy as np
from config import EMBEDDING_DIM, TOP_K
from utils.embeddings import get_embeddings
from services.text_processing import extract_text_from_pdf, chunk_text
from utils.embeddings import get_query_embedding
from services.llm_integration import generate_answer_with_llm


def initialize_faiss():
    # Extract and chunk text
    text = extract_text_from_pdf("ncert_text.pdf")
    chunks = chunk_text(text)

    # Generate embeddings and create FAISS index
    embeddings = get_embeddings(chunks)
    index = faiss.IndexFlatL2(EMBEDDING_DIM)
    index.add(np.array(embeddings).astype('float32'))

    # Map chunk indices to text for easy retrieval
    chunk_map = {i: chunk for i, chunk in enumerate(chunks)}
    return index, chunk_map

def search_faiss(user_query, index, chunk_map):
    # Convert user query to an embedding
    query_embedding = get_query_embedding(user_query)

    # Search in FAISS
    D, I = index.search(query_embedding, TOP_K)

    # Retrieve text chunks from chunk_map
    relevant_chunks = [chunk_map[idx] for idx in I[0]]

    # Generate a comprehensive answer using Flan-T5
    answer = generate_answer_with_llm(user_query, relevant_chunks)
    return answer
