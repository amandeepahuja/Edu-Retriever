


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
5. **User Interface**: A Streamlit interface allows users to input questions and receive responses from the system, providing an accessible UI for testing.

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

## Future Improvements
- **Fine-tune the Language Model**: Customize the Flan-T5 model on the NCERT dataset for more specific responses.
- **Chunk Selection Optimization**: Improve the selection of context chunks for more precise and relevant answers.
- **Enhanced UI with Streamlit**: Add features such as question history, confidence scores, and answer summaries.
- **Caching Common Responses**: Store frequently asked questions and responses to speed up the response time.

## FAQ

**Q1: What is Retrieval-Augmented Generation (RAG)?**  
**A:** RAG is a technique that combines information retrieval with natural language generation, enabling systems to pull in relevant data and then generate responses. It’s especially useful for question-answering and information-based applications.

**Q2: Can I use a different LLM instead of Flan-T5?**  
**A:** Yes, you can replace Flan-T5 with other transformer models available on Hugging Face, such as GPT-J or GPT-NeoX. You would need to modify the model loading and inference code accordingly.

**Q3: Why use FAISS for retrieval?**  
**A:** FAISS is optimized for fast, scalable similarity search, making it suitable for finding the most relevant text chunks in large datasets efficiently.

## Troubleshooting

- **Issue**: `OSError: [WinError 2] The system cannot find the file specified`  
  **Solution**: Run the command prompt as an administrator or use the `--user` flag when installing packages.

- **Issue**: `Error: Could not retrieve response.`  
  **Solution**: Ensure that the FastAPI server is running, and verify the API URL and endpoint configuration.

- **Issue**: Slow response times on Streamlit interface.  
  **Solution**: Consider upgrading hardware resources (e.g., using a GPU) or optimizing the model by using a smaller variant of Flan-T5.

## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request. For significant changes, please discuss them in an issue first.

## Acknowledgments
- **Hugging Face** for providing access to pre-trained language models.
- **Facebook AI Research (FAIR)** for FAISS, a powerful tool for fast similarity search.
- **NCERT** for providing the educational content used in this demonstration.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

---

This README file now includes additional sections covering **Technologies Used**, **Architecture Overview**, **FAQ**, **Troubleshooting**, and **Acknowledgments**. This structure ensures that your README is informative, organized, and accessible for users and contributors. Let me know if there’s anything else you’d like to add!
