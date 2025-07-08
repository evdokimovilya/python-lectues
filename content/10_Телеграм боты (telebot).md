# Телеграм боты с использованием библиотеки telebot

**Telebot** - наиболее простая библиотека для создания телеграм ботов. 

Документация: 
https://github.com/eternnoir/pyTelegramBotAPI

Примеры ботов, написанных с использованием этой библиотеки: 
https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples

## Установка

```bash
pip install pytelegrambotapi
```
## Основы

Импорт и инициализация бота. Вставьте свой токен, который вы получили от BotFather

```python
import telebot

TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)
```

## 📌 Хэндлеры

Хэндлеры - это функции, которые отвечают за обработку сообщений пользователя. В параметрах хэндлера можно указывать

- На какой тип сообщения реагировать
- Какой текст должен быть у сообщения
- ...


#### 1. **Команды** (/start, /help, и т.п.)

```python
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Я твой бот.")
```

#### 2. **Обычные текстовые сообщения**


```python
@bot.message_handler(func=lambda message: message.text == "Привет")
def text_handler(message):
    bot.send_message(message.chat.id, "Привет-привет!")
```


#### 3. **Текстовые сообщения определенного шаблона (регулярные выражения)**


Обрабатывает любые сообщения где есть **привет**
```python
@bot.message_handler(regexp='привет')
def hello(message):
    bot.send_message(message.chat.id, "Отвечаю на все, где есть 'привет'!")
```

Обрабатывает только сообщение **привет как дела**
```python
@bot.message_handler(regexp='^привет как дела$')
def hello_how(message):
    bot.send_message(message.chat.id, "Отвечаю только на привет как дела!")
```

#### 4. **Фильтр по типу контента**

```python
@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    bot.send_message(message.chat.id, "Красивая картинка!")
```

#### 5. **Фильтр под данным в инлайн кнопке**

```python
@bot.callback_query_handler(func=lambda call: call.data == "like")
def handle_like(call):
    bot.answer_callback_query(call.id, "Спасибо за лайк!")
    bot.send_message(call.message.chat.id, "Вы поставили 👍")
```
## 🧮 Кнопки

Кнопки - еще один интерфейс для общения с ботом. Кнопки бывают двух видов: 
- Обычные - показываются в самом низу экрана, под строкой ввода сообщения
- Инлайн - показываются в самих сообщения от бота

### 1. **Обычные (ReplyKeyboardMarkup)**

```python
from telebot import types

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("📥 Добавить"), types.KeyboardButton("Список"))
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)
```

- Они отображаются **внизу экрана** и остаются активными.
- Удобны для основных действий.

### 3. **Инлайн-кнопки (InlineKeyboardMarkup)**

```python
@bot.message_handler(commands=['inline'])
def inline_buttons(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Нажми меня", callback_data="pressed")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Инлайн-кнопка:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call.data == 'pressed')
def handle_callback(call):
	bot.answer_callback_query(call.id, "Кнопка нажата!")
	bot.send_message(call.message.chat.id, "Вы нажали кнопку.")
```

- Кнопки встроены **в сообщение**.
- Позволяют реализовать меню, голосование, пагинацию.

Обратите внимание, что тут используется **callback_query_handler**. 


## 🔄 Пошаговый диалог (state machine)

Частым сценарием в боте является ведения диалога с пользователем, который состоит из нескольких этапов. Например: 
- Введи имя 
- Введи фамилию
- Введи возраст

В это случае мы хотим уметь указывать, какой хэндлер должен срабатывать после определенного шага. 

В **telebot** за это отвечает **bot.register_next_step_handler**

Например, этот бот  сначала спрашивает имя пользователя, потом фамилию и только потом сохраняет все в словарь. 

```python
import telebot

  
TOKEN = ''
bot = telebot.TeleBot(TOKEN)

users = {}
  
# 🟢 Команда /start
@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, "👋 Привет! Жми /add")

  
@bot.message_handler(commands=['add'])
def ask_name(message):
    bot.send_message(message.chat.id, "Введите свое имя:")
     # переход к следующему шагу
    bot.register_next_step_handler(message, ask_last_name)


@bot.message_handler(content_types=['text'])
def ask_last_name(message):
    name = message.text.strip()
    if not name:
        bot.send_message(message.chat.id, "❗ Имя не может быть пустым.")
        return
        
    bot.send_message(message.chat.id, f"Приятно познакомиться, {name}!")
    bot.send_message(message.chat.id, f"Вводи фамилию:")
    
    # переход к следующему шагу
    bot.register_next_step_handler(message, save_user, name)

  
def save_user(message, name):
    last_name = message.text.strip()
    if not last_name:
        bot.send_message(message.chat.id, "❗ Фамилия не может быть пустой.")
        return
    print('Имя:', name, 'Фамилия:', last_name)

    # сохраним пользователя в словаре
    users[message.from_user.id] = {'name': name, 'last_name': last_name}
    bot.send_message(message.chat.id, f"Я тебя сохранил")


# 🔘 Запуск
bot.infinity_polling()
```



