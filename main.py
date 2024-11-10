# main.py

from fastapi import FastAPI
from agent.smart_agent import smart_agent
from services.faiss_index import initialize_faiss, search_faiss

app = FastAPI()

# Initialize FAISS index and chunk map on startup
index, chunk_map = initialize_faiss()

# Endpoint for directly querying the RAG system
@app.post("/query/")
async def query_rag_system(user_query: str):
    enhanced_answer = search_faiss(user_query, index, chunk_map)
    return {"response": enhanced_answer}

# Endpoint for the smart agent
@app.post("/agent/")
async def agent_endpoint(user_query: str):
    return await smart_agent(user_query, index, chunk_map)
