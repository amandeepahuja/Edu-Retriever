# streamlit_app.py

import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

def get_answer_from_agent(user_query):
    try:
        response = requests.post(f"{FASTAPI_URL}/agent/?user_query=\"{user_query}\"")
        if response.status_code == 200:
            return response.json().get("response", "No response available.")
        else:
            return "Error: Could not retrieve response."
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("RAG System with LLM")
    st.write("Ask questions and receive detailed answers from a retrieval-augmented generation (RAG) system using FAISS and Flan-T5.")

    user_query = st.text_input("Enter your question")
    if st.button("Get Answer"):
        if user_query:
            with st.spinner("Fetching answer..."):
                answer = get_answer_from_agent(user_query)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
