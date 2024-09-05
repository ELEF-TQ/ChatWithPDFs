import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings.huggingface import  HuggingFaceInstructEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings 
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFaceHub
from ui import css, bot_template, user_template

# Function to extract text from uploaded PDFs
@st.cache_data
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    if not text:
        st.error("No text could be extracted from the uploaded PDFs.")
    return text 

# Function to split the extracted text into smaller chunks for processing
def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

# Function to create a vectorstore from text chunks
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# Function to create a conversation chain for the chat
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# Function to handle user input and generate a response
def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.error("Please start the conversation by uploading PDF documents first.")
        return
    
    with st.spinner("Generating response..."):
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

# Main function for the Streamlit app
def main():
    load_dotenv()
    
    st.set_page_config(page_title="ChatWithPDF", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    
    # Initialize conversation and chat history in session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Chat with your PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    
    if user_question:
        handle_userinput(user_question)
        
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDF documents ...", accept_multiple_files=True)
       
        if st.button("Start"):
            if pdf_docs is None or len(pdf_docs) == 0:
                st.error("Please upload at least one PDF document.")
            else:
                # Clear previous chat history when new PDFs are uploaded
                st.session_state.chat_history = None
                
                with st.spinner("Loading ..."):
                    # Extract PDF text
                    raw_text = get_pdf_text(pdf_docs)
        
                    # Split text into chunks
                    text_chunks = get_text_chunks(raw_text)
        
                    # Create vector store from text chunks
                    vectorstore = get_vectorstore(text_chunks)

                    # Create conversation chain
                    st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == '__main__':
    main()
