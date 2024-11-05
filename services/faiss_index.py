# services/faiss_index.py

import faiss
import numpy as np
from config import EMBEDDING_DIM, TOP_K
from utils.embeddings import get_embeddings
from services.text_processing import extract_text_from_pdf, chunk_text

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

def search_faiss(query, index, chunk_map):
    from utils.embeddings import get_query_embedding
    query_embedding = get_query_embedding(query)

    # Search for the top K matches
    D, I = index.search(query_embedding, TOP_K)
    relevant_chunks = [chunk_map[idx] for idx in I[0]]
    return relevant_chunks
