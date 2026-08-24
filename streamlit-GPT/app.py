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

api_key = st.secrets.get("GROQ_API_KEY")

if input_text:
    if not api_key:
        st.error("Please add your GROQ_API_KEY in Streamlit App Settings -> Secrets.")
    else:
        try:
            llm = ChatGroq(
                model_name="llama-3.1-8b-instant",
                groq_api_key=api_key.strip()
            )
            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser
            response = chain.invoke({"question": input_text})
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")