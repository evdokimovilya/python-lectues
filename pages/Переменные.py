import streamlit as st

st.title("🧑‍🏫 Лекция 1: Переменные в Python")

with open("content/Переменные.md", "r", encoding="utf-8") as f:
    content = f.read()
st.markdown(content, unsafe_allow_html=True)
