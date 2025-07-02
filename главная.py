import streamlit as st
import os

st.set_page_config(page_title="Лекции по Python", layout="centered")

st.title("📘 Лекции по программированию на Python")
st.markdown("Выберите лекцию из списка ниже либо в меню слева.")

for file in os.listdir("pages"):
    st.page_link(f"pages/{file}", label=file.replace('_', '.'))



