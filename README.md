# RAG System with FAISS and Flan-T5

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
9. [Future Improvements](#future-improvements)
10. [FAQ](#faq)
11. [Troubleshooting](#troubleshooting)
12. [Contributing](#contributing)
13. [Acknowledgments](#acknowledgments)
14. [License](#license)

## Overview
The goal of this project is to demonstrate a RAG pipeline that combines **retrieval** and **generation**. Given a question, the system retrieves relevant information from a dataset (extracted text from NCERT PDFs) using FAISS, and then generates a coherent response using a pre-trained open-source language model (Flan-T5). This approach enables more accurate and contextually aware responses to questions on the dataset.

## Features
- **Retrieval using FAISS**: Efficient vector-based similarity search to retrieve relevant chunks of information.
- **Language Generation with Flan-T5**: Open-source language model for natural, coherent answer generation.
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
