import streamlit as st


with open("content/Работа с файлами..md", "r", encoding="utf-8") as f:
    content = f.read()
    
st.markdown(content, unsafe_allow_html=True)


products = [{'name':  'яблоко', 'price': 100}, {'name': 'картошка', 'price': 50}, {'name': 'молоко', 'price': 80}]