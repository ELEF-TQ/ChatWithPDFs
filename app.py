import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import HuggingFaceHub
# from htmlTemplates import css, bot_template, user_template



def main():
    st.set_page_config(page_title="ChatWithPDF",page_icon=":books")
    st.header("Chat with your PDFs :books:")
    st.text_input("Ask a question about your documents:")
    
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("upload your PDF documents ...")
        st.button("Start")




if __name__ == '__main__':
    main()