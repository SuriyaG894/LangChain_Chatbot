from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

## for Langsmith tracing

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")

##Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. you response to user query."),
        ("user","Question:{question}")
    ]
)

## streamlit
st.title("Langchain demo with Ollama Model")
input_text = st.text_input("Search for a topic")

##LLM Model
llm = Ollama(model="llama3.2:3b")
##Output Parser
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
