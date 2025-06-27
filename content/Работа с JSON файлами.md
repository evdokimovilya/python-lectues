# Работа с JSON файлами


**JSON (JavaScript Object Notation)** — это текстовый формат обмена данными, легко читаемый человеком и машиной.

Несмотря на происхождение от JavaScript, формат считается независимым от языка и может использоваться практически с любым языком программирования. Для многих языков существует готовый код для создания и обработки данных в формате JSON.

**Примеры JSON:**

```json
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "skills": ["Python", "SQL", "Git"]
}
```

**Базовые правила JSON:**

| Правило                                         | Пример                 | Комментарий                      |
| ----------------------------------------------- | ---------------------- | -------------------------------- |
| Данные хранятся в парах **ключ: значение**      | "name": "Иван"`        | Ключ — всегда строка             |
| Используются только **двойные кавычки**         | "ключ": "значение"`    | Одинарные — не допускаются       |
| Разделение элементов через **запятую**          | "a": 1, "b": 2`        | Как в Python-словаре             |
| Структура — **объекты** {} и **массивы** []     | { "list": [1, 2, 3] }` |                                  |
| Логические и пустые значения: true, false, null |                        | Аналоги Python:True, False, None |

**JSON ↔ Python: соответствие типов**

| JSON         | Python           |
| ------------ | ---------------- |
| object     | dict           |
| array      | list           |
| string     | str            |
| number     | int, float   |
| true/false | True / False |
| null       | None           |
### **2. Модуль "json"  в Python**

Встроенный модуль Python для работы с JSON:

```python
import json
```

### **3. Чтение из файла**

```python
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
```


### **4. Запись JSON (в строку и файл)**

```python
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

🔹 ensure_ascii=False — сохраняет кириллицу  
🔹 indent=4 — форматирует вывод (удобно читается)

### 5.  **Структура JSON может быть простой или вложенной**

JSON-файлы могут содержать как **плоские** структуры (ключ-значение), так и **сложные вложенные** объекты и списки.

🔹 Пример 1: Плоская структура

```json
{
  "name": "Алиса",
  "age": 28,
  "city": "Москва"
}
```

🔸 Пример 2: Вложенная структура

```json
{
  "name": "Боб",
  "age": 35,
  "address": {
    "city": "Санкт-Петербург",
    "street": "Невский проспект",
    "zip": "190000"
  },
  "phones": ["+7 911 000-00-00", "+7 812 123-45-67"]
}

```
### Пример полной работы

```python
import json

person = {
    "name": "Олег",
    "age": 40,
    "languages": ["Python", "JavaScript"],
    "is_admin": False
}

# Сохраняем в файл
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)

# Читаем из файла
with open("person.json", "r", encoding="utf-8") as f:
    loaded_person = json.load(f)

print(loaded_person["languages"]) 
```


## **Где используется JSON**

### 📌 JSON — один из самых популярных форматов передачи данных в современных приложениях.

---

### 💡 Где именно его применяют:

#### **1. Веб-сайты и браузеры**

- JavaScript в браузере получает данные от сервера в формате JSON;
- пример: подгрузка товаров в интернет-магазине без перезагрузки страницы.


```json
{   "id": 1001,   "name": "Кофеварка",   "price": 5490 }
```
---

####  **2. REST API и запросы к серверу**

- Практически все современные API (Telegram, GitHub, Яндекс, OpenAI и др.) используют JSON.
- Пример HTTP-запроса:

```nginx

GET https://api.example.com/users/42
```

Ответ:

```json
{   "id": 42,   "username": "alice",   "email": "alice@example.com" }
```

---

#### **3. Конфигурационные файлы**

- Многие программы и библиотеки используют `.json` для хранения настроек:
    

```json
{   "theme": "dark",   "autosave": true,   "language": "ru" }
```

#### **4. Хранение данных (вместо БД на старте)**

- На ранних этапах проектов JSON можно использовать как простой формат хранения локальных данных (без базы данных).

#### **5. Логирование и обмен между сервисами**

- Микросервисы и приложения передают друг другу события в виде JSON-сообщений.

#### Пример подгрузки товаров на сайте Wildberries


```json
{
    "state": 0,
    "version": 2,
    "payloadVersion": 2,
    "data": {
        "products": [
            {
                "id": 225020084,
                "__sort": 83801,
                "ksort": 0,
                "time1": 2,
                "time2": 167,
                "wh": 507,
                "dtype": 4,
                "dist": 3446,
                "root": 202543237,
                "kindId": 0,
                "brand": "Aiyin",
                "brandId": 311415837,
                "siteBrandId": 0,
                "colors": [],
                "subjectId": 793,
                "subjectParentId": 858,
                "name": "Термопринтер этикеток штрихкодов для маркетплейсов",
                "entity": "принтеры",
                "matchId": 228853829,
                "supplier": "Aiyin Official",
                "supplierId": 1420933,
                "supplierRating": 4.7,
                "supplierFlags": 12224,
                "pics": 8,
                "rating": 5,
                "reviewRating": 4.8,
                "nmReviewRating": 4.8,
                "feedbacks": 133,
                "nmFeedbacks": 133,
                "panelPromoId": 1003454,
                "promoTextCard": "ЛЕТНЯЯ ВЫГОДА",
                "promoTextCat": "ЛЕТНЯЯ ВЫГОДА",
                "volume": 16,
                "viewFlags": 1581136,
                "sizes": [
                    {
                        "name": "",
                        "origName": "0",
                        "rank": 0,
                        "optionId": 356622493,
                        "wh": 507,
                        "time1": 2,
                        "time2": 167,
                        "dtype": 4,
                        "price": {
                            "basic": 345900,
                            "product": 282600,
                            "total": 292400,
                            "logistics": 9800,
                            "return": 0
                        },
                        "saleConditions": 134217728,
                        "payload": "SXHZWca0QDEa2yprtG4H5irPF3ylp767cE5oKHxkNOpVjDkBcKC2NOyz1cFWT7w8ko8/Zpxo9j0CYxhWqg"
                    }
                ],
                "totalQuantity": 12,
                "logs": "MlC1ddZj+3s/UCUzi2Hx2ZsAz5I/rhtVqXLysBzaj/cAYBxJ3cCdntKo6P15nqb87LYs0mMk",
                "meta": {
                    "tokens": []
                }
            },
            {
                "id": 181460723,
                "__sort": 66146,
                "ksort": 0,
                "time1": 2,
                "time2": 167,
                "wh": 507,
                "dtype": 4,
                "dist": 3446,
                "root": 165411348,
                "kindId": 0,
                "brand": "YUNKAI",
                "brandId": 310996888,
                "siteBrandId": 0,
                "colors": [
                    {
                        "name": "розовый",
                        "id": 16761035
                    }
                ],
                "subjectId": 3625,
                "subjectParentId": 858,
                "name": "Набор термобумаги для термопринтера 13 шт",
                "entity": "принтеры портативные",
                "matchId": 122631687,
                "supplier": "YUNKAI",
                "supplierId": 1404612,
                "supplierRating": 4.8,
                "supplierFlags": 12224,
                "pics": 2,
                "rating": 5,
                "reviewRating": 4.9,
                "nmReviewRating": 4.9,
                "feedbacks": 447,
                "nmFeedbacks": 447,
                "panelPromoId": 1003753,
                "promoTextCard": "ХИТ ПРОДАЖ",
                "promoTextCat": "ХИТ ПРОДАЖ",
                "volume": 5,
                "viewFlags": 1581121,
                "sizes": [
                    {
                        "name": "",
                        "origName": "0",
                        "rank": 0,
                        "optionId": 299649761,
                        "wh": 507,
                        "time1": 2,
                        "time2": 167,
                        "dtype": 4,
                        "price": {
                            "basic": 50300,
                            "product": 34900,
                            "total": 36100,
                            "logistics": 1200,
                            "return": 0
                        },
                        "saleConditions": 134217728,
                        "payload": "QvIMuWaKOXxDNtXTmCPhj6j/6699KKL/1yJqv832ujmshKlt6lAe+9VwTwjHb9JzbDUS333O3CzChOU"
                    }
                ],
                "totalQuantity": 239,
                "logs": "MopdBpvQLH3R8kPmlpGzzvvv+hii8xETpHA5QateqNTpCaSeGgRBCcBdM0q9hzX1i20+YCk",
                "meta": {
                    "tokens": []
                }
            },
            {
                "id": 201111861,
                "__sort": 63247,
                "ksort": 0,
                "time1": 2,
                "time2": 167,
                "wh": 507,
                "dtype": 4,
                "dist": 3446,
                "root": 179603760,
                "kindId": 0,
                "brand": "Ok Store",
                "brandId": 111190,
                "siteBrandId": 0,
                "colors": [],
                "subjectId": 3625,
                "subjectParentId": 858,
                "name": "Бумага для мини принтера самоклеящаяся",
                "entity": "принтеры портативные",
                "matchId": 105408305,
                "supplier": "Ok Store",
                "supplierId": 3946726,
                "supplierRating": 4.8,
                "supplierFlags": 12224,
                "pics": 3,
                "rating": 5,
                "reviewRating": 4.9,
                "nmReviewRating": 4.9,
                "feedbacks": 745,
                "nmFeedbacks": 745,
                "panelPromoId": 1003454,
                "promoTextCard": "ЛЕТНЯЯ ВЫГОДА",
                "promoTextCat": "ЛЕТНЯЯ ВЫГОДА",
                "volume": 2,
                "viewFlags": 1581056,
                "sizes": [
                    {
                        "name": "",
                        "origName": "0",
                        "rank": 0,
                        "optionId": 324887727,
                        "wh": 507,
                        "time1": 2,
                        "time2": 167,
                        "dtype": 4,
                        "price": {
                            "basic": 34600,
                            "product": 23400,
                            "total": 24200,
                            "logistics": 800,
                            "return": 0
                        },
                        "saleConditions": 134217728,
                        "payload": "EGGKdKiW40Yi6LPP21yol9+K/vap3GUyQnQ5cwcJVvalmV1MJv74wKPfRq4l4nwfHB8CWRgvBonfYfw"
                    }
                ],
                "totalQuantity": 6,
                "meta": {
                    "tokens": []
                }
            }
        ]
    }
}

```
