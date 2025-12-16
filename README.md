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
│       ├── main.py  
│       ├── database.py  
│       ├── models.py  
│       ├── schemas.py  
│       ├── seed_data.py  
│       ├── routers/  
│       │   ├── authors.py  
│       │   ├── categories.py  
│       │   ├── articles.py  
│       │   ├── comments.py  
│       │   └── summary.py  
│       └── frontend/  
│           ├── index.html  
│           ├── app.js  
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
