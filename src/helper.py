import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY is None:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

# Set the Google API Key in the environment
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""  # Handle None
        except Exception as e:
            print(f"Error reading {pdf}: {e}")
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    # Specify the appropriate model for embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # Update model name if needed
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

def get_conversational_chain(vector_store):
    # Use GoogleGenerativeAI as the LLM for ConversationalRetrievalChain
    llm = GoogleGenerativeAI(model="gemini-1.5-pro")  # Update this model name as necessary
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain
