import streamlit as st

st.set_page_config(page_title="Лекции по Python", layout="centered")

st.title("📘 Лекции по программированию на Python")
st.markdown("Выберите лекцию из списка ниже либо в меню слева.")

st.page_link("pages/1_Переменные.py", label="1.Переменные")
st.page_link("pages/2_Функция Input. Типы данных.py", label="2.Input. Типы данных")
st.page_link("pages/3_Условные операторы.py", label="3.Условные операторы")
st.page_link("pages/4_Работа с файлами.py", label="4.Работа с файлами")
st.page_link("pages/5_Работа с json.py", label="5.Работа с JSON файлами")



