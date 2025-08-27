
import streamlit as st
import re

def convert_backticks_to_bold(text):
    # Обрабатываем блоки кода отдельно
    parts = []
    last_pos = 0
    
    # Находим все блоки кода (между ```)
    for match in re.finditer(r'```.*?```', text, re.DOTALL):
        # Текст до блока кода
        before = text[last_pos:match.start()]
        parts.append(re.sub(r'`([^`]+)`', r'**\1**', before))
        
        # Сам блок кода (оставляем без изменений)
        parts.append(match.group(0))
        last_pos = match.end()
    
    # Остаток текста после последнего блока кода
    remaining_text = text[last_pos:]
    parts.append(re.sub(r'`([^`]+)`', r'**\1**', remaining_text))
    
    return "".join(parts)

# Основной код страницы
with open(r"content/14_Телеграм боты (telebot).md", "r", encoding="utf-8") as f:
    content = f.read()
    
rendered = convert_backticks_to_bold(content)
st.markdown(rendered)
