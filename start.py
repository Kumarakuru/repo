#!pip install langchain
import streamlit as st, openai, os, json
import streamlit.components.v1 as components 
from langchain.indexes  import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader



#setup Open AI
ai_key="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"
os.environ["OPENAI_API_KEY"] = ai_key

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
html_string=F"<div font-size=3px>Powered by chatGPT</div><br>{result}"
st.markdown(html_string, unsafe_allow_html=True);

components.html(cv_text,height=2000,scrolling=True )   