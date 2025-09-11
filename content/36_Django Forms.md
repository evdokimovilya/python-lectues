## Django Forms. 

#### Введение

Работа с формами – одна из ключевых задач в веб-разработке. 

Пользовательский ввод необходим почти в каждом проекте: регистрация, авторизация, поиск, комментарии, загрузка файлов и многое другое. 

Мы посмотрели, как обрабатывать формы вручную. В результате получили много кода, загруженного условными операторами для валидации. Если повторять эту рутину для обработки каждой формы на сайте - получится система, которую сложно поддерживать. 

Поэтому Django предоставляет мощный и удобный инструмент для работы с формами – **Django Forms**. Он абстрагирует многие рутинные вещи, вам нужно лишь описать структуру и больше думать о бизнес-логике. 

#### Что умеют 

1. **Валидация данных**
2. **Генерация HTML**
3. **Защита от ошибок и атак**
4. **Удобная работа с моделями**
![фвыа](http://images.na4u.ru/static/django6/1.png)


#### Основные компоненты Django Forms

1. **Классы форм** (`forms.Form`, `forms.ModelForm`).
2. **Поля** (`CharField`, `EmailField`, `IntegerField`, `FileField` и др.).
3. **Виджеты** (отвечают за отображение поля в HTML: текстовое поле, чекбокс, select-список и т.д.).
4. **Методы валидации** (`clean()`, `clean_<fieldname>()`).

## Пример использования Django Forms

В предыдущей главе мы описывали обработку формы добавления книг на сайт. Давайте перепишем ее с использованием новой библиотеки. 

### Создание класса с формой

Ключевой компонент джанго формс - класс, описывающий форму. Он очень похож на модельные классы, которые мы пишем для таблиц. 

1. Создайте файлик forms.py в корне проекта
2. Создайте класс, наследующийся от forms.Form
3. Внутри класса опишите поля, которые должны быть в вашей форме 

```python
from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=255, label='название книги')
    author = forms.CharField(max_length=255, label='автор книги')
    price = forms.IntegerField(label='цена книги')
```

![фвыа](http://images.na4u.ru/static/django6/2.png)
### Отрисовка формы

Создайте новую функцию-представление, в которой создайте экземпляр класса формы. Передайте его в контекст нового шаблона. 

```python
def add_book_with_form(request):
    form = BookForm()
    context = {'form': form}

    return render(request, 'add_book_with_form.html', context)
```

![фвыа](http://images.na4u.ru/static/django6/3.png)

Создайте новый url адрес для новой формы

```python
from django.urls import path

from .views import hello, books, add_book, add_book_with_form

urlpatterns = [
    path('', hello),
    path('books', books),
    path('books/add', add_book),
    path('books/add_with_form', add_book_with_form),
]
```

![фвыа](http://images.na4u.ru/static/django6/4.png)
Создайте шаблон для новой формы. В шаблоне теперь не будет необходимости описывать все поля. Достаточно передать переменную с формой внутри тэга forms. И не забывать указать {% csrf_token %}

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Страница книг</title>
</head>
<body>

<h1>Добавление книги</h1>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Добавить</button>
</form>

</body>
</html>
```

![фвыа](http://images.na4u.ru/static/django6/5.png)

![фвыа](http://images.na4u.ru/static/django6/6.png)
### Обработка формы

Приступим к этапу обработки формы. 

Напишите **print(request.POST)** в представлении, нажмите на кнопку отправки формы. Посмотрите, что в консоли отображается словарь с данными. 
![фвыа](http://images.na4u.ru/static/django6/7.png)

Обратите внимание, что названия полей совпадают с названиями, определенными в классе с формой. 


Дальше надо следовать алгоритму:
1. Проверить, что запрос имеет метод POST
2. Если да - проверить валидность данных
3. Если валидно - получить данные для каждого поля 
4. Создать объект модели на основе данных
5. Если невалидно - отобразить форму с ошибками 

```python
def add_book_with_form(request):

    form = BookForm()
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            price = form.cleaned_data['price']

            Book.objects.create(
                title=title,
                author=author,
                price=price
            )
            return redirect('/books')
        
    context = {'form': form}

    return render(request, 'add_book_with_form.html', context)
```

![фвыа](http://images.na4u.ru/static/django6/8.png)
![фвыа](http://images.na4u.ru/static/django6/9.png)

![фвыа](http://images.na4u.ru/static/django6/10.png)
## Добавление поля с выбором категории

Категория книги - связанное с другой таблице поле. Поэтому его привязка к форму выглядит чуть сложнее.

Добавьте в форму новое поле с типом ModelChoiceField. В аргументах передайте параметр queryset, в котором укажите все объекты из таблицы Category. 

![фвыа](http://images.na4u.ru/static/django6/11.png)

Поле с категорией после этого должно автоматически появиться в форме. 

![фвыа](http://images.na4u.ru/static/django6/12.png)
В представлении добавьте получение поля с категорией, в добавлении новой книги передайте категорию. 

![фвыа](http://images.na4u.ru/static/django6/13.png)

![фвыа](http://images.na4u.ru/static/django6/14.png)

![фвыа](http://images.na4u.ru/static/django6/15.png)