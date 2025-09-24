## Bootstrap 

#### 1. Что такое Bootstrap?

Bootstrap — это популярный CSS-фреймворк с открытым исходным кодом, который используется для быстрой и удобной разработки адаптивных и современных веб-интерфейсов. Он был создан компанией **Twitter** и впервые выпущен в 2011 году.

**Основные цели Bootstrap:**
- Ускорить процесс верстки.
- Обеспечить единый стиль интерфейса.
- Сделать сайты адаптивными для разных устройств.

#### 2. Структура Bootstrap

Bootstrap включает три ключевых компонента:

1. **CSS** — стили для типографики, сетки, форм, кнопок и других элементов.
2. **JavaScript** (часто с использованием библиотеки Popper.js) — добавляет интерактивные элементы: модальные окна, выпадающие меню, карусели.
3. **Иконки и готовые компоненты** — множество UI-элементов для ускорения разработки.

#### 3. Подключение Bootstrap
Есть два основных способа подключения:

1. **Через CDN**:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```
2. **Локально** — скачивание файлов и подключение из проекта

#### 4. Компоненты Bootstrap

Bootstrap предлагает готовые компоненты. Вы можете найти код этих компонентов в документации, а потом использовать их в своих проектах

- **Кнопки** (`.btn`, `.btn-primary`, `.btn-success`).
- **Формы** с валидацией.
- **Навигация** (`.navbar`).
- **Карточки** (`.card`).
- **Модальные окна** (`.modal`).
- **Карусели** (`.carousel`).


#### 5.  Некоторые примеры: 



**Форма**
![фвыа](http://images.na4u.ru/static/bootstrap/1.png)

```html
<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```


**Карточка с текстом и картинкой** 

![фвыа](http://images.na4u.ru/static/bootstrap/2.png)

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```


**Шаблон для целой страницы**

![фвыа](http://images.na4u.ru/static/bootstrap/3.png)

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Новости о Луне</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
</head>
<body>

<!-- Навигация -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">Лунные Новости</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Переключить навигацию">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link active" href="#">Главная</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Исследования</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Календарь событий</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Контакты</a></li>
      </ul>
    </div>
  </div>
</nav>

<!-- Заголовок -->
<header class="bg-light py-5 text-center">
  <div class="container">
    <h1 class="display-4">Новости о Луне</h1>
    <p class="lead">Свежие новости и исследования нашей ближайшей соседки в космосе</p>
  </div>
</header>

<!-- Основной контент -->
<main class="container my-5">
  <div class="row g-4">

    <!-- Новость 1 -->
    <div class="col-md-4">
      <div class="card h-100 shadow-sm">
        <img src="https://example.com/moon-landing.jpg" class="card-img-top" alt="Посадка на Луну" />
        <div class="card-body d-flex flex-column">
          <h5 class="card-title">Новая миссия на Луну стартует в 2026</h5>
          <p class="card-text flex-grow-1">НАСА объявило о запуске новой миссии Artemis III, которая доставит людей на Луну в 2026 году.</p>
          <a href="#" class="btn btn-primary mt-auto">Читать далее</a>
        </div>
        <div class="card-footer text-muted">18 сентября 2025</div>
      </div>
    </div>

    <!-- Новость 2 -->
    <div class="col-md-4">
      <div class="card h-100 shadow-sm">
        <img src="https://example.com/lunar-research.jpg" class="card-img-top" alt="Исследования Луны" />
        <div class="card-body d-flex flex-column">
          <h5 class="card-title">Обнаружены новые минералы на Луне</h5>
          <p class="card-text flex-grow-1">Международная команда ученых обнаружила уникальные минералы в лунных породах, что может изменить представления о геологии Луны.</p>
          <a href="#" class="btn btn-primary mt-auto">Читать далее</a>
        </div>
        <div class="card-footer text-muted">15 сентября 2025</div>
      </div>
    </div>

    <!-- Новость 3 -->
    <div class="col-md-4">
      <div class="card h-100 shadow-sm">
        <img src="https://example.com/lunar-base.jpg" class="card-img-top" alt="Лунная база" />
        <div class="card-body d-flex flex-column">
          <h5 class="card-title">Проект лунной базы планируется к запуску</h5>
          <p class="card-text flex-grow-1">Китай объявил о планах построить постоянную исследовательскую базу на Луне к 2030 году.</p>
          <a href="#" class="btn btn-primary mt-auto">Читать далее</a>
        </div>
        <div class="card-footer text-muted">10 сентября 2025</div>
      </div>
    </div>

  </div>
</main>

<!-- Футер -->
<footer class="bg-dark text-white text-center py-4 mt-auto">
  <div class="container">
    &copy; 2025 Лунные Новости. Все права защищены.
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
```


#### 6. Система сетки (Grid System)

![фвыа](http://images.na4u.ru/static/bootstrap/4.png)

Сердце Bootstrap — это **сетка**, основанная на Flexbox.

- Сетка делится на 12 колонок.
- Используются контейнеры (`.container`, `.container-fluid`).
- Ряды (`.row`) содержат колонки (`.col`).
- Пример:
    

```
<div class="container">
  <div class="row">
    <div class="col-6">Левая часть</div>
    <div class="col-6">Правая часть</div>
  </div>
</div>
```

Адаптивность достигается с помощью классов:

- `.col-sm-*` — для маленьких экранов.
- `.col-md-*` — для средних.
- `.col-lg-*` — для больших.

#### 7. Ютилити-классы

Bootstrap имеет множество вспомогательных классов для управления:

- Отступами (`.m-3`, `.p-2`).
- Цветами (`.text-primary`, `.bg-dark`).
- Выравниванием (`.text-center`, `.d-flex`, `.justify-content-between`).

#### 8. Альтернативы Bootstrap

- Tailwind CSS
- Foundation
- Bulma
- Materialize