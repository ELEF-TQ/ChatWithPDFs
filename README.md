# RAG Application: ChatWithPDFs

## Overview
ChatWithPDF is a Python application that enables AI-powered interactions with multiple PDF documents. Using LangChain for advanced text processing and Retrieval-Augmented Generation (RAG) for context-aware responses, this application provides intelligent answers based on the content of your PDFs.

## Features
- **AI-Powered Chat:**: Users can ask questions about the content of multiple uploaded PDF documents.
- **Contextual Responses:**: Delivers accurate answers based on the documents' text using LangChain and RAG.
- **Efficient Document Processing:**: Reads multiple PDFs, extracts text, and embeds it for seamless interactions.
- **Text Chunking:**: Divides text into manageable chunks for effective processing and retrieval.


## Technologies Used
- **LangChain:** Framework for linking the various components of the RAG system.
- **Streamlit:** For creating the interactive web interface.
- **OpenAI API:** For generating AI-driven responses.
- **Hugging Face (hkunlp/instructor-xl):**  Embedding functions for accurate information retrieval and Text generation model.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/chatwithpdfs.git
    cd chatwithpdfs
    ```


2. . **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Start the development server**:
    ```bash
   streamlit run app.py
    ```

## Configuration
Ensure you have the following environment variables set up:

- `OPENAI_API_KEY`
- `HUGGINGFACEHUB_API_TOKEN`
- 

You can set these environment variables in a `.env` file at the root of your project.

## Usage
1. Load multiple PDF documents into the app by following the provided instructions.
2. Ask questions in natural language about the loaded PDFs using the chat interface.

## Project Structure
![PDF-LangChain](https://github.com/user-attachments/assets/c8ed6e32-84d0-4010-a621-b3c89a1f7eed)


## Demo video
https://github.com/user-attachments/assets/c9cf0b9b-3ab8-487b-9c68-af1b0c7b773b

