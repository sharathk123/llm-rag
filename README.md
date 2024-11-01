# PDF Querying Application

This application allows users to upload PDF files into a FAISS vector database and query the content of those PDFs. It utilizes LangChain, Google Gemini for embedding, and Streamlit for the user interface.

## Features

- Upload multiple PDF files
- Extract and store content from PDFs in a FAISS vector database
- Query the content of the PDFs using natural language questions
- Interactive web-based interface built with Streamlit

## Technologies Used

- **LangChain**: A framework for building applications with language models.
- **Google Gemini**: A generative AI model used for embeddings.
- **Streamlit**: A Python library for creating web applications for data science and machine learning.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.

## Installation

1. Clone the repository:
   git clone https://github.com/sharathk123/llm-rag.git
   cd llm-rag
2. Create a new virtual environment (optional but recommended)
   pip install -r requirements.txt
3. Install the required packages
   pip install -r requirements.txt
4. Set up environment variables
   Create a .env file in the project root directory and add your Google API key:
   GOOGLE_API_KEY=your_google_api_key

## Usage

1. **Run the Streamlit application:**  
   Open your terminal or command prompt and execute the following command:
   streamlit run app.py
2. **Open the application:**
   After running the command, your default web browser should automatically open. If it does not, navigate to http://localhost:8501 in your web browser.
3. **Upload PDF files:**
   Use the file uploader in the sidebar to select and upload one or multiple PDF files.
4. **Ask questions:**
   Once the PDFs are processed, enter questions related to the content of the PDFs in the provided input box.
   The application will retrieve and display relevant answers based on the content of the uploaded PDFs.

