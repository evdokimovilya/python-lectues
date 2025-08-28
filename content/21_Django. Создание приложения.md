## Django 1. Создание приложения.


Djnago - популярный фреймворк для создания веб-приложений на питоне. 

## Алгоритм создания простого приложения 

Рассмотрим по шагам как создать приложение на Джанго, которое выводит "Hello world" на главной странице 

### 1. Настройка окружения

1. Создайте папку с проектом

![фвыа](http://images.na4u.ru/static/django1/1.png)

2. Откройте в Pycharm
![фвыа](http://images.na4u.ru/static/django1/2.png)
3. Установите python
![фвыа](http://images.na4u.ru/static/django1/3.png)

![фвыа](http://images.na4u.ru/static/django1/4.png)


![фвыа](http://images.na4u.ru/static/django1/5.png)


Иногда бывает, что pycharm не сразу видит созданное окружение питона. Поэтому можно выбрать его  самим. 

![фвыа](http://images.na4u.ru/static/django1/6.png)

![фвыа](http://images.na4u.ru/static/django1/7.png)


### Установка библиотеки

![фвыа](http://images.na4u.ru/static/django1/8.png)

![фвыа](http://images.na4u.ru/static/django1/9.png)


### Создание проекта и первого приложения

1. Откройте терминал
![фвыа](http://images.na4u.ru/static/django1/10.png)

2. Введите команду 
```
   django-admin startproject my_project .
   ```
![фвыа](http://images.na4u.ru/static/django1/11.png)
 
 ![фвыа](http://images.na4u.ru/static/django1/12.png)
 2. Введите команду 
```
   django-admin startapp core
   ```
 ![фвыа](http://images.na4u.ru/static/django1/13.png)
  
  Должна появиться папка с приложением
  ![фвыа](http://images.na4u.ru/static/django1/14.png)
 
 Каждое новое приложение в джанго необходимо регистрировать. То есть прописывать его имя в общем списке приложений. Его можно найти в настройках -- settings.py
 ![фвыа](http://images.na4u.ru/static/django1/15.png)
### Создание первого представления

Откройте файл views.py в папке core. В этом файле будут жить все функции-обработчики веб запросов для приложения core. 

Напишите функцию, которая просто возвращает приветствие: 

![фвыа](http://images.na4u.ru/static/django1/16.png)

 ![фвыа](http://images.na4u.ru/static/django1/17.png)

### Подключение представления к url адресу 

Для того, чтобы созданная функция отрабатывала при переходе не главную страницу -- надо указать это в джанге. Это делается с помощью файлов urls.py.

Создайте файл urls.py в папке core. Укажите в нем соответствие пустого пути (так как эта главная страница) и названия вашей функции. 

 ![фвыа](http://images.na4u.ru/static/django1/18.png)
 ![фвыа](http://images.na4u.ru/static/django1/19.png)
 
 Джанго автоматически создает главный urs.py файлик, в котором надо подключать остальные urls.py файлы приложений. Этот шаг надо сделать один раз после создания приложения. 

Откройте в папке my_project файл urls.py. Подключите внутри него urls.py файл вашего приложения с помощью функции include, которую надо импортировать. 
 ![фвыа](http://images.na4u.ru/static/django1/20.png) 
### Запуск сервера


Введите команду 
```
python manage.py runserver
```
 ![фвыа](http://images.na4u.ru/static/django1/21.png)

 ![фвыа](http://images.na4u.ru/static/django1/22.png)
 
 Перейдите в браузере по адресу, который выдался в консоли.
 На главной странице должна появиться строка, которую вы возвращали в функции hello
 ![фвыа](http://images.na4u.ru/static/django1/23.png)