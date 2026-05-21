# Lab 6 — DevOps, Docker, CI/CD

## Опис проєкту

Даний проєкт демонструє контейнеризацію Python-додатку за допомогою Docker та автоматизацію процесу CI/CD через GitHub Actions.

Проєкт включає:

* Dockerfile;
* Docker Compose;
* PostgreSQL контейнер;
* автоматичне тестування через pytest;
* CI/CD pipeline;
* GitHub Actions.

---

# Використані технології

* Python 3.11
* Flask
* Docker
* Docker Compose
* PostgreSQL
* GitHub Actions
* Pytest

---

# Структура проєкту

```text
lab-5/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── controllers/
├── dto/
├── models/
├── repositories/
├── services/
├── tests/
│
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── app.py
└── README.md
```

---

# Запуск через Docker

## Побудова Docker image

```bash
docker-compose build
```

## Запуск контейнерів

```bash
docker-compose up
```

---

# Контейнери

Після запуску створюються:

* python_app — Flask додаток;
* python_tests — контейнер для тестів;
* postgres_db — PostgreSQL база даних.

---

# Локальний запуск

## Встановлення залежностей

```bash
pip install -r requirements.txt
```

## Запуск додатку

```bash
python app.py
```

---

# Змінні середовища

| Змінна            | Опис                  |
| ----------------- | --------------------- |
| FLASK_ENV         | Режим Flask           |
| POSTGRES_USER     | Користувач PostgreSQL |
| POSTGRES_PASSWORD | Пароль PostgreSQL     |
| POSTGRES_DB       | Назва бази даних      |

---

# API Endpoint

| Endpoint | Метод | Опис             |
| -------- | ----- | ---------------- |
| /        | GET   | Головна сторінка |

---

# Запуск тестів

```bash
pytest
```

---

# Перевірка роботи

Після запуску Docker додаток буде доступний за адресою:

```text
http://localhost:5000
```

---

# CI/CD Pipeline

GitHub Actions автоматично:

* встановлює залежності;
* запускає автоматичні тести;
* виконує збірку Docker image.

---

# GitHub Repository

GitHub repository:

```text
https://github.com/Vitalik2234/lab-6-refactoring
```

---

# Результат роботи

У результаті роботи було:

* виконано контейнеризацію Python-проєкту;
* налаштовано Docker Compose;
* створено PostgreSQL контейнер;
* реалізовано CI/CD через GitHub Actions;
* автоматизовано запуск тестів та збірку Docker image.
