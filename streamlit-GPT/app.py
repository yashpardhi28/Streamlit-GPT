from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("My GPT")
input_text = st.text_input("What question do you have in mind?")

# Ollama
llm = OllamaLLM(model="gemma2:2b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# Output
if input_text:
    st.write(chain.invoke({"question": input_text}))