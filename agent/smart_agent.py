# agent/smart_agent.py

from services.faiss_index import search_faiss

async def smart_agent(user_query: str, index, chunk_map):
    greetings = ["hello", "hi", "hey", "greetings"]
    if user_query.lower() in greetings:
        return {"response": "Hello! How can I assist you today?"}

    # Check if query is a simple math expression
    if any(op in user_query for op in ["+", "-", "*", "/"]):
        try:
            result = eval(user_query)  # Basic eval, be cautious in production
            return {"response": f"The result is {result}"}
        except:
            return {"response": "Sorry, I couldn't evaluate the expression."}

    # If neither greeting nor math, use RAG system
    enhanced_answer  = search_faiss(user_query, index, chunk_map)
    return {"response": enhanced_answer }
