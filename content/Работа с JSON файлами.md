# Работа с JSON файлами


**JSON (JavaScript Object Notation)** — это текстовый формат обмена данными, легко читаемый человеком и машиной.

Несмотря на происхождение от JavaScript, формат считается независимым от языка и может использоваться практически с любым языком программирования. Для многих языков существует готовый код для создания и обработки данных в формате JSON.

Примеры JSON:

```json
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "skills": ["Python", "SQL", "Git"]
}
```


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

