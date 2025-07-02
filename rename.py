import os
import re

order = ['Переменные', 
         'Функция Input. Типы данных',
         'Условные операторы',
         'Методы строк',
         'Работа с файлами',
         'Работа с JSON файлами',
         'Функции',
         'Телеграм боты (telebot)']


VAULT_PATH = "content"

files = sorted([f for f in os.listdir(VAULT_PATH) if f.endswith(".md")])
for number, name in enumerate(order, start=1):
    for file in files:
        file_name = re.findall('[А-я, A-z, ().]+', file)[0]
        if name == file_name:
            new_name = f'{number}_{name}.md'
            os.rename(os.path.join(VAULT_PATH, file), os.path.join(VAULT_PATH, new_name))
            break