# utils/embeddings.py

from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once to use across the project
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embeddings(chunks):
    return model.encode(chunks)

def get_query_embedding(query):
    query_embedding = model.encode([query]).astype('float32')
    return np.array(query_embedding)
