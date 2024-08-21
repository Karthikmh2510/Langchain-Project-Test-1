# Here we are trying to create a simple Chat Bot
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
openai_key = os.getenv('OPENAI_API_KEY')
#Let's create a function to load OpenAI model and get some response

def get_openai_response(question):
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.5, api_key=openai_key)
    response = llm(question)
    return response

# Let's initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Small LangChain Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask any question")

# If ask button is clicked,
if submit and input:
    response = get_openai_response(input)
    st.subheader("The Response is: ")
    st.write(response)

