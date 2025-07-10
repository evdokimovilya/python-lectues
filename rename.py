import os
import re

order = ['Переменные', 
         'Функция Input. Типы данных',
         'Условные операторы',
         'Методы строк',
         'Циклы. For. While',
         'Работа с файлами',
         'Работа с JSON файлами',
         'Функции',
         'Функции. Области видимости.',
         'Телеграм боты с нуля',
         'Телеграм боты (telebot)',
         'Базы данных. Введение',
         'Базы данных. SQL',
         'Yandex API'
         ]


VAULT_PATH = "content"

files = sorted([f for f in os.listdir(VAULT_PATH) if f.endswith(".md")])
for number, name in enumerate(order, start=1):
    for file in files:
        file_name = re.findall('([А-яA-Za-z()\. ]+)\.md', file)[0]
        print(file_name)
        if name == file_name:
            new_name = f'{number}_{name}.md'
            os.rename(os.path.join(VAULT_PATH, file), os.path.join(VAULT_PATH, new_name))
            break