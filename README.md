# Blog_admin
Курсовой проект студента Чаликова Евгения группы М7О-507С-21
# Административная панель коллективного блога  
### FastAPI + MySQL + Docker + Frontend (HTML/JS)

Проект представляет собой учебное веб-приложение для управления контентом коллективного блога.  
Реализована REST API на FastAPI, база данных MySQL, контейнеризация через Docker и простой фронтенд на HTML/JS.

---

## Функциональные возможности

### Статьи
- Просмотр всех статей  
- Фильтрация по статусу  
- Фильтрация по автору  

### Комментарии
- Просмотр всех комментариев  
- Фильтрация по статье  

### Сводные отчёты
- Таблица «Управление контентом»  
- Отчёт «Активность авторов»  

### Frontend
- Интерфейс просмотра данных в таблицах  
- Фильтры и кнопки обновления  
- Автоматическая загрузка данных при открытии страницы

---

## Веб-приложение

<img width="1919" height="862" alt="image" src="https://github.com/user-attachments/assets/d6d8b13e-4be5-4943-a0f0-9d011e7222b0" />

### Таблицы представления данных
- Статьи (с возможностью поиска по ID)
- Комментарии (с возможностью поиска по ID)
- Управление контентом (сводная таблица)
- Активность авторов (сводный отчёт)

---

## Swagger UI

<img width="1350" height="879" alt="image" src="https://github.com/user-attachments/assets/3786663e-89cf-4556-8c18-0fec9e701b21" />

### API-эндпоинты
- GET /authors/ — получение списка всех авторов
- POST /authors/ — создание нового автора

- GET /categories/ — получение списка всех категорий
- POST /categories/ — создание новой категории

- GET /articles/ — получение списка всех статей
- POST /articles/ — создание новой статьи

- GET /comments/ — получение списка всех комментариев
- POST /comments/ — создание нового комментария

- GET /summary/content-management — получение сводного отчёта по управлению контентом
- GET /summary/author-activity — получение отчёта по активности авторов

---

## Стек технологий

Backend: FastAPI, Python, SQLAlchemy, Pydantic  
Database: MySQL 8  
Frontend: HTML, CSS, JavaScript  
DevOps: Docker, Docker Compose  

---

## Структура проекта

```text
blog-admin/  
├── docker-compose.yml  
├── backend/  
│   ├── Dockerfile  
│   ├── requirements.txt  
│   └── app/  
│       ├── database.py  
│       ├── main.py  
│       ├── models.py  
│       ├── schemas.py  
│       ├── routers/  
│       │   ├── articles.py  
│       │   ├── authors.py  
│       │   ├── categories.py  
│       │   ├── comments.py  
│       │   └── summary.py  
│       └── frontend/  
│           ├── app.js  
│           ├── index.html  
│           └── styles.css  
└── README.md  
```
---

## Быстрый запуск

Перейдите в каталог проекта:  
```bash
cd blog-admin
```

Запустите приложение:
```bash
docker-compose up --build
```

Приложение будет доступно по адресу:
```text
http://localhost:8000/
```

Документация API автоматически доступна по адресу:
```text
http://localhost:8000/docs
```
