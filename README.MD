# Allure Examples (API only)

Мини-проект на `pytest + requests + allure`.

## Что сделано по заданию

1. Создан проект
2. Подготовлена тестовая документация через Allure (лейблы, stories, titles, categories, environment).
3. Настроен запуск из Allure.

## Стек

- `pytest`
- `requests`
- `allure-pytest`

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Allure отчет

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

или

```bash
allure serve allure-results
```

## Сценарии

- `GET /posts/{id}`
- `GET /posts?userId=`
- `POST /posts`

Тесты используют публичный API: `https://jsonplaceholder.typicode.com`, поэтому выполняются без токенов.
