import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("My GPT")
input_text = st.text_input("What question do you have in mind?")

# Retrieve key from Streamlit Secrets
api_key = st.secrets.get("GROQ_API_KEY")

if input_text:
    if not api_key:
        st.error("Please add your GROQ_API_KEY in Streamlit App Settings -> Secrets.")
    else:
        llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=api_key)
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
        st.write(chain.invoke({"question": input_text}))