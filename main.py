import streamlit as st

st.title('Hello World')
st.write('This is a simple Streamlit app.')
  
if st.button("say hello"):
    st.text("hello streamlit")

name=st.text_input("please enter your name: ")
if name:
    st.write(f'hello,{name}!')