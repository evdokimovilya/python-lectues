import streamlit as st
import os

st.set_page_config(page_title="Лекции по Python", layout="centered")

st.title("📘 Лекции по программированию на Python")
st.markdown("Выберите лекцию из списка ниже либо в меню слева.")

files = sorted([f for f in os.listdir('pages') if f.endswith(".py")], key=lambda x: int(x.split('_')[0]))
for file in files:
    st.page_link(f"pages/{file}", label=file.replace('_', '.')[:-3])



