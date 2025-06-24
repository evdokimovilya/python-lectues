import streamlit as st


with open("content/Работа с файлами..md", "r", encoding="utf-8") as f:
    content = f.read()
    
st.markdown(content, unsafe_allow_html=True)
