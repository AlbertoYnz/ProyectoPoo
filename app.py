import streamlit as st

prompt = st.chat_input("Say something")

if prompt:
    st.write(prompt)

with st.chat_message("user"):
    st.write("Hello 👋")

with st.chat_message("assistant"):
    st.write("Hello 👋")