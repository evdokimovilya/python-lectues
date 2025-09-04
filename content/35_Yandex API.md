# Работа с Yandex API

Yandex API - набор инструментов от Яндекса, которые можно использовать для написания своих программ. 

Например: 
- Yandex GPT - для интеграции в свои программы нейросете
- Yandex Speech - для генерации и распознавания текста 
- ...

Для того, чтобы начать пользоваться АПИ, необходимо зарегистрироваться в Yandex Cloud. 
АПИ платное, но цена не очень высокая. Особенно, если вы просто тестируете функции для себя, когда количество запросов небольшое. 

## Получение АПИ ключа

### Регистрация в Yandex Cloud

1. Зайдите на сайт https://yandex.cloud/ru
2. Нажимаете "Подключиться"
	![фвыа](http://images.na4u.ru/static/yandex/1.jpg)
3. Далее выполнили первые два  шага из туториала https://yandex.cloud/ru/docs/getting-started/individuals/registration
	1. Создайте платежный аккаунт
	2. После регистрации Яндекс должен выдать стартовый грант, поэтому самим деньги можно не класть.


У тебя должна появиться подобная панель управления
	![фвыа](http://images.na4u.ru/static/yandex/2.jpg)


### Получение ключа АПИ

Теперь необходимо получить ключ АПИ для нужного инструмента. Например, мы хотим получить ключ для Yandex GPT

1. **Нажмите на вкладку Identity and Access Management**
		![фвыа](http://images.na4u.ru/static/yandex/3.jpg)



2. **Нажмите Create Service Account**
		![фвыа](http://images.na4u.ru/static/yandex/4.jpg)






3. Выберите имя для аккаунта
		![фвыа](http://images.na4u.ru/static/yandex/5.jpg)
4. Выберите роль ai --> admin
		![фвыа](http://images.na4u.ru/static/yandex/6.jpg)
5. Нажмите create
6. Выберите созданный аккаунт в списке
7. Нажмите Create new key ---> Create API key
		![фвыа](http://images.na4u.ru/static/yandex/7.jpg)
8. В открывшемся окне введите название, выберите доступные методы с помощью "Select all"
	![фвыа](http://images.na4u.ru/static/yandex/8.jpg)
9. Скопируйте полученный АПИ ключ
	![фвыа](http://images.na4u.ru/static/yandex/9.jpg)

## Работа с АПИ

Документация для работы с Yandex GPT находится [по этому адресу](https://yandex.cloud/ru/docs/foundation-models/quickstart/yandexgpt
В этом разделе находятся туториалы, примеры работы с разными нейросетками. 

Нам необходим [раздел Text Generation](https://yandex.cloud/en/docs/foundation-models/text-generation/api-ref/TextGeneration/completion)

В это разделе приведена документация работы с методом, который позволит получать ответы от Yandex GPT нейросети по запросам. 

Основным наполнением любого запроса к АПИ является json, который необходимо отправлять вместе запросом.

Рассмотрим, минимальную рабочую версию json. Если следовать документации, она должна выглядеть так. 

```json
{
    "modelUri": f"gpt://<folder_ID>/yandexgpt",
    "completionOptions": {
        "stream": False,
        "temperature": 0.4,
        "maxTokens": 100,
        "reasoningOptions": {
            "mode": "DISABLED"
        }
    },
    "messages": [
        {
            "role": "user",
            "text": "расскажи про философоию",
        }
    ]
}
```

**modeUri** - адрес GPT модели, можно [выбирать другую версию](https://yandex.cloud/en/docs/foundation-models/concepts/yandexgpt/models)
**temperature** - степень вариативности ответов
**maxTokens** - максимальное количество токенов на каждый ответ
**mode** - должна ли модель дольше думать. Можно выбрать другой вариант
**messages**
- role - может быть user, system, assistant
	- user - сообщение от пользователя
	- system - инструкции для модели
	- assistant - предыдущие ответы модели, чтобы хранить контекст диалога
- text - текст сообщения

Также на этой странице есть описания и других полей, которые не являются обязательными. 

Обратите внимание, что в **modelUri** надо вставить свой **folder_ID**

**Где взять folder_id**
![фвыа](http://images.na4u.ru/static/yandex/10.jpg)

### Выполнение запроса

Для того чтобы выполнить запрос, надо отправить сформированный выше json по адресу. 

Адрес согласно документации: 
https://llm.api.cloud.yandex.net/foundationModels/v1/completion

Получаем следующий код на Python:

Вместо API_TOKEN и CATALOG надо вставить свои значения. 

```python
import requests


url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
API_TOKEN = 'AQVN2fasdfasdfuKmCTGvcGZfvlaH8'
CATALOG = 'b1gt123123ndncqf33o7'

  
payload = {
    "modelUri": f"gpt://{CATALOG}/yandexgpt",
    "completionOptions": {
        "stream": False,
        "temperature": 0.4,
        "maxTokens": 100,
        "reasoningOptions": {
            "mode": "DISABLED"
        }
    },
    "messages": [
        {
            "role": "user",
            "text": "расскажи про философоию",
        }
    ]
}

  
headers = {'Authorization': f"Api-Key {API_TOKEN}"}
res = requests.post(url, json=payload, headers=headers)
print(res.json())
```

Результат: 

```json
{'result': {'alternatives': [{'message': {'role': 'assistant', 'text': 'Философия — это особая форма познания мира, вырабатывающая систему знаний о фундаментальных принципах и основах человеческого бытия. Она стремится понять и объяснить мир, человека и его место в нём, а также основные принципы и законы, которые определяют развитие природы, общества и мышления.\n\nФилософия занимается вопросами, которые не всегда поддаются научному или религиозному объяснению. Она исследует такие темы, как смысл жизни, свобода, справедливость, добро 
и зло, истина, красота и другие.\n\nОсновные направления философии'}, 'status': 'ALTERNATIVE_STATUS_TRUNCATED_FINAL'}], 'usage': {'inputTextTokens': '15', 'completionTokens': '100', 'totalTokens': '115', 'completionTokensDetails': {'reasoningTokens': '0'}}, 'modelVersion': '09.02.2025'}}
```

Видно, что ответ пришел. Осталось только достать его из нужного поля в словаре. 

