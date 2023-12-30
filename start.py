import streamlit as st
import openai

title = st.text_input('Whats your Name', '')
html_string=F"My Name is:<b>{title}</b>"
st.markdown(html_string, unsafe_allow_html=True)

st.title("Kumara Personal Info !!!")

for i in range(50): 
  st.write("Hello, world!, here comes Kumara !!!")
