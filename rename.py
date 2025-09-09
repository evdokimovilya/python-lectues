import os
import re

order = ['Переменные', 
         'Функция Input. Типы данных',
         'Условные операторы',
         'Методы строк',
         'Циклы. For. While',
         'Списки',
         'Словари',
         'Работа с файлами',
         'Работа с JSON файлами',
         'Функции',
         'Функции. Области видимости',
         'ООП. Введение',
         'ООП. Связывание классов',
         'ООП. Паттерн MVC',
         'ООП. Абстрактные классы',
         'ООП. Принципы',
         'ООП. SOLID. Паттерны',
         'Графические приложения',
         'Телеграм боты с нуля',
         'Телеграм боты (telebot)',
         'Базы данных. Введение',
         'Базы данных. SQL',
         'Базы данных. Нормальные формы',
         'Базы данных. Работа c python',
         'Базы данных. ORM',
         'Веб. Клиент-сервер. HTTP',
         'Веб. GET запрос. Параметры',
         'Веб. POST'
         ' запросы',
         'Django. Введение',
         'Django. Создание приложения',
         'Django. Работа с базой данных',
         'Django. Работа с шаблонами',
         'Django. GET запросы. Фильтрация',
         'Django. POST запросы. Добавление данных',
         'Django. Доп.Материалы',
         'Yandex API',
         'GIT. Системы контроля версий',
         'GIT. Туториал по созданию репозитория',
         'Литература'
         ]


VAULT_PATH = "content"

files = sorted([f for f in os.listdir(VAULT_PATH) if f.endswith(".md")])
for number, name in enumerate(order, start=1):
    for file in files:
        file_name = re.findall('([А-яA-Za-z()\.\- ]+)\.md', file)[0]
        print(name, file_name, name==file_name)
        if name == file_name:
            print(file_name)
            new_name = f'{number}_{name}.md'
            os.rename(os.path.join(VAULT_PATH, file), os.path.join(VAULT_PATH, new_name))
            break