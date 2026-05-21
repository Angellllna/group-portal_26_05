# group-portal_26_05

## Структура проєкту

```
group-portal_26_05/
├── config/                # Налаштування Django-проєкту
│   ├── __init__.py
│   ├── asgi.py            # ASGI-конфігурація
│   ├── settings.py        # Основні налаштування проєкту
│   ├── urls.py            # Головний маршрутизатор URL
│   └── wsgi.py            # WSGI-конфігурація
├── venv/                  # Віртуальне середовище
├── .gitignore
├── manage.py              # Утиліта управління Django
└── README.md
```

## Інструкція Як працювати з Git (GitFlow)

1. Перейти на `main` та оновити його:

   ```bash
   git checkout main
   git pull origin main
   ```

2. Подивитися свій таск у Trello.
   Назва гілки = ID таска, наприклад: `FOR-2`, `GL-3`, `AUTH-1` тощо.

3. Створити гілку від `main`:

   ```bash
   git checkout -b FOR-2
   ```

4. Зробити зміни в коді, запустити проєкт і перевірити, що все працює.

5. Додати файли та зробити коміт:

   ```bash
   git add .
   git commit -m "FOR-2 — коротко-що-робиш"
   ```

6. Відправити гілку на GitHub:

   ```bash
   git push origin FOR-2
   ```
