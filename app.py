# Import necessary modules
import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

# Set up Streamlit page configuration
st.set_page_config("Information Retrieval")

def user_input(user_question):
    """
    Handles user input for the information retrieval system.
    Retrieves response from the conversation chain and displays chat history.

    Args:
        user_question (str): The question input by the user.
    """
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']

    # Display chat history
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write("User:", message.content)
        else:
            st.write("Reply:", message.content)

def main():
    """
    Main function to run the Streamlit application.
    Sets up the UI components for file upload, text input, and information retrieval processing.
    """
    st.header("Information Retrieval System 💁")

    # Capture user question from input field
    user_question = st.text_input("Ask a Question from the PDF Files")

    # Initialize session state variables if not already set
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None

    # Process user input if a question is provided
    if user_question:
        user_input(user_question)

    # Sidebar for PDF file upload and processing
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader(
            "Upload your PDF Files and Click on the Submit & Process Button",
            accept_multiple_files=True
        )
        
        # Process PDFs when the submit button is clicked
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                # Extract text from uploaded PDFs
                raw_text = get_pdf_text(pdf_docs)

                # Split text into chunks for vector storage
                text_chunks = get_text_chunks(raw_text)

                # Create vector store with text chunks
                vector_store = get_vector_store(text_chunks)

                # Initialize conversation chain with vector store
                st.session_state.conversation = get_conversational_chain(vector_store)
                
                st.success("Done")

# Run main function when script is executed
if __name__ == "__main__":
    main()
