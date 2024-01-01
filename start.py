import streamlit as st
import openai
import streamlit.components.v1 as components 
from langchain.document_loaders import TextLoader
from langchain.indexes  import VectorstoreIndexCreator
import openai, os

#setup Open AI
ai_key="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"
openai.api_key = ai_key
os.environ["OPENAI_API_KEY"] = ai_key;

#Initialize langchain
loader = TextLoader(r'cv.json')
index = VectorstoreIndexCreator().from_loaders([loader])

# Open a file: file
file = open('cv.html',mode='r')
# read all lines at once
cv_text = file.read() 
# close the file
file.close() 

query = st.text_input("What's on Your Mind? Ask Me About Anything Specific", '')
result=index.query(query)
html_string=F"<div font-size=3px>Powered by chatGPT</div><br>Response for your query is:<b>{result}</b>"
st.markdown(html_string, unsafe_allow_html=True);


#components.html(,height=500,scrolling=True)


components.html(cv_text,height=2000,scrolling=True )
    

