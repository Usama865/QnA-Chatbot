from helper import create_vector_database, get_qa_chain
import streamlit as st

st.title("QnA Chatbot by Codebasics🌱")

question= st.text_input("Question:",placeholder='Write your question here')
if question:
    chain=get_qa_chain()
    response= chain(question)
    answer=response['result']

    st.header("Answer:")
    st.write(answer)