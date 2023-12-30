import streamlit as st
import openai

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.write("OK Imported !!!")

st.title("Kumara Personal Info !!!")

for i in range(50): 
  st.write("Hello, world!, here comes Kumara !!!")
