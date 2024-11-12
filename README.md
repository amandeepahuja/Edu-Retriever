
# Edu-Retriever

This project implements a **Retrieval-Augmented Generation (RAG)** system using **FAISS** for similarity search and **Flan-T5** as the language model to generate detailed answers based on NCERT text data. The application is served via **FastAPI** and includes an interactive UI built with **Streamlit** to allow users to input questions and receive responses from the system.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Technologies Used](#technologies-used)
5. [Architecture Overview](#architecture-overview)
6. [Setup Instructions](#setup-instructions)
7. [Usage](#usage)
8. [Example Queries](#example-queries)
9. [Additional Agent Actions](#additional-agent-actions)
10. [Future Improvements](#future-improvements)

## Overview
The goal of this project is to demonstrate a RAG pipeline that combines **retrieval** and **generation**. Given a question, the system retrieves relevant information from a dataset (extracted text from NCERT PDFs) using FAISS, and then generates a coherent response using a pre-trained open-source language model (Flan-T5). This approach enables more accurate and contextually aware responses to questions on the dataset.

## Features
- **Retrieval using FAISS**: Efficient vector-based similarity search to retrieve relevant chunks of information.
- **Language Generation with Flan-T5**: Open-source language model for natural, coherent answer generation.
- **Smart Agent with Custom Actions**: An intelligent agent that can perform different actions based on user intent.
- **FastAPI Backend**: RESTful API to handle requests and interact with the RAG components.
- **Streamlit Interface**: A user-friendly interface for querying the RAG system and displaying answers.

## Project Structure

```plaintext
rag_system/
├── main.py                   # Entry point for FastAPI server
├── requirements.txt          # Python dependencies
├── config.py                 # Configuration settings (e.g., model names, API URLs)
├── services/
│   ├── faiss_index.py        # FAISS initialization and search functions
│   ├── text_processing.py    # PDF text extraction and chunking utilities
│   └── llm_integration.py    # Language model integration for response generation
├── utils/
│   └── embeddings.py         # Embedding utilities for vectorizing text
├── agent/
│   └── smart_agent.py        # Smart agent logic for determining actions based on queries
└── streamlit_app.py          # Streamlit application for interactive querying
```

## Technologies Used

- **Python**: Core programming language for the application.
- **FAISS**: Facebook’s library for fast vector similarity search.
- **Flan-T5**: A fine-tuned version of T5, optimized for language tasks.
- **FastAPI**: Python web framework for building APIs.
- **Streamlit**: Python library for building interactive web applications.
- **Hugging Face Transformers**: Library for working with pre-trained language models.

## Architecture Overview

1. **Text Processing**: The NCERT text data is extracted and split into manageable chunks for embedding.
2. **Vector Embedding**: The chunks are embedded using pre-trained models and stored in a FAISS index.
3. **Query Handling**: A query from the user is processed, embedded, and compared to the stored vectors in FAISS to retrieve relevant text chunks.
4. **Response Generation**: Retrieved text chunks are fed into Flan-T5 to generate a coherent response.
5. **Smart Agent Actions**: The agent interprets user intent and invokes different actions based on keywords in the query.
6. **User Interface**: A Streamlit interface allows users to input questions and receive responses from the system, providing an accessible UI for testing.

## Setup Instructions

### Prerequisites
- Python 3.8 or later
- Virtual environment (recommended)
- Basic familiarity with Python libraries and API calls

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rag-system
cd rag-system
```

### 2. Install Dependencies
Install the required packages with pip:

```bash
pip install -r requirements.txt
```

### 3. Configure the Application
In `config.py`, you can configure model paths, API keys, and other constants. Make sure to review any model-specific configurations if needed.

### 4. Start the FastAPI Server
Launch the FastAPI server on `http://127.0.0.1:8000`:

```bash
uvicorn main:app --reload
```

### 5. Run the Streamlit Interface
In a new terminal, start the Streamlit app to access the UI at `http://localhost:8501`:

```bash
streamlit run streamlit_app.py
```

## Usage

### Querying the RAG System via API
Once the FastAPI server is running, you can send requests to it directly.

- **Endpoint**: `/agent/`
- **Method**: POST
- **Data**: JSON with a `user_query` field

#### Example cURL Command
```bash
curl -X POST "http://127.0.0.1:8000/agent/" -H "Content-Type: application/json" -d '{"user_query": "How does sound travel through different mediums?"}'
```

### Using the Streamlit Interface
1. Open your browser and go to `http://localhost:8501`.
2. Enter a question in the input box (e.g., "How does sound travel through different mediums?").
3. Click "Get Answer" to see the response generated by the RAG system.

## Example Queries

Here are a few example questions that can be asked based on the NCERT dataset:

1. **"How does sound travel through different mediums?"**
2. **"What is the difference between compression and rarefaction?"**
3. **"Why can't sound travel in a vacuum?"**

## Additional Agent Actions

The smart agent can interpret the user’s intent and invoke different actions based on the query. Here are the available actions:

1. **Knowledge Expansion Mode**:
   - **Description**: Provides extended background or context on the topic.
   - **Trigger Keywords**: `"learn more about"`, `"expand on"`
   - **Example Query**: `"Learn more about photosynthesis"`
   - **Expected Response**: `"Here’s some extended information on photosynthesis: [generated context from Flan-T5]"`

2. **Quiz Generator Mode**:
   - **Description**: Generates a set of quiz questions on the topic.
   - **Trigger Keywords**: `"quiz me on"`, `"practice questions on"`
   - **Example Query**: `"Quiz me on sound waves"`
   - **Expected Response**: 
     ```
     Here are some practice questions on sound waves:
     1. What is sound?
     2. Explain the concept of rarefaction.
     3. What factors affect the speed of sound?
     ```

3. **Fun Fact Mode**:
   - **Description**: Provides an interesting fact about a given topic.
   - **Trigger Keywords**: `"fun fact about"`, `"tell me something interesting about"`
   - **Example Query**: `"Tell me a fun fact about black holes"`
   - **Expected Response**: `"Did you know? Black holes can slow down time due to their intense gravity!"`

## Future Improvements
- **Fine-tune the Language Model**: Customize the Flan-T5 model on the NCERT dataset for more specific responses.
- **Context Management**: Improve the agent’s ability to retrieve context-specific information dynamically.
- **Enhanced UI with Streamlit**: Add features such as question history, confidence scores, and answer summaries.
- **Caching Common Responses**: Store frequently asked questions and responses to speed up the response time.
