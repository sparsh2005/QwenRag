import streamlit as st
from main import main

st.title("QwenRag: Your Agentic RAG System")

user_query = st.text_input("Ask me anything:")

if user_query:
    st.write("Processing your query...")
    final_output = main(user_query)
    st.write("Final Answer:", final_output) 