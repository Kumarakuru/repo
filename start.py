import streamlit as st
import openai
import streamlit.components.v1 as components 

initial_text="This is start only !!!"

# Open a file: file
file = open('cv.html',mode='r')
# read all lines at once
cv_text = file.read() 
# close the file
file.close() 

query = st.text_input('You wanted to know specifics, enter your question', '')
html_string=F"<div font-size=3px>Powered by chatGPT</div><br>Response for your query is:<b>{query}</b>"
st.markdown(html_string, unsafe_allow_html=True);


if len(query)>0:
    cv_text="Query Done !!!"

#st.markdown(cv_text,unsafe_allow_html=True);

components.html(cv_text,height=2000,scrolling=True )
    

