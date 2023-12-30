import streamlit as st
import openai

initial_text="This is start only !!!"

# Open a file: file
file = open('cv.html',mode='r')
# read all lines at once
cv_text = file.read() 
# close the file
file.close() 

query = st.text_input('Enter Your Query About Kumara !!', '')
html_string=F"Response for your query is:<b>{query}</b>"
st.markdown(html_string, unsafe_allow_html=True);


if len(query)>0:
    cv_text="Query Done !!!"

#st.markdown(cv_text,unsafe_allow_html=True);

st.components.v1.html(cv_text,height=200)
