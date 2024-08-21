# Conversational Q&A ChatBot

import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

# Starting streamlit UI
st.set_page_config(page_title="Conversational Q&A ChatBot")
st.header("Hey let's chat!")


from dotenv import load_dotenv
load_dotenv()

import os
openai_key = os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(temperature=0.5, api_key=openai_key)

if 'flowmessage' not in st.session_state:
    st.session_state['flowmessage'] = [
        SystemMessage(content="Yor are a Comedian AI assistant")
    ]

def get_chatmodel_response(question):
    
    st.session_state['flowmessage'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessage'])
    st.session_state['flowmessage'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Input: ", key="input")
submit = st.button("Ask any question")

# If ask button is clicked,
if submit and input:
    response = get_chatmodel_response(input)
    st.subheader("The Response is: ")
    st.write(response)