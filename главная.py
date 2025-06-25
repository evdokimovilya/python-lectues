import streamlit as st

st.set_page_config(page_title="Лекции по Python", layout="centered")

st.title("📘 Лекции по программированию на Python")
st.markdown("Выберите лекцию из списка ниже либо в меню слева.")

st.page_link("pages/1_Переменные.py", label="Переменные")
st.page_link("pages/2_Функция Input. Типы данных.py", label="Input. Типы данных")
st.page_link("pages/3_Условные операторы.py", label="Условные операторы")
st.page_link("pages/4_Работа с файлами.py", label="Работа с файлами")


