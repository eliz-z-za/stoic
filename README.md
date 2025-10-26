# Stoic Diary API

API для стоического дневника настроения. Позволяет записывать свои эмоции и получать стоические комментарии и цитаты.

## Быстрый старт

### Установка

```bash
# Установка зависимостей
pip3 install -r requirements.txt
```

### Запуск

```bash
uvicorn main:app --reload
```

Сервер запустится на `http://localhost:8000`

## API Endpoints

- `GET /` - Информация об API
- `POST /entries` - Добавить запись в дневник
- `GET /entries` - Получить все записи
- `GET /analytics/mood` - Статистика по настроению

## Документация

После запуска откройте в браузере:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Примеры использования

### Добавить запись

```bash
curl -X POST "http://localhost:8000/entries" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "date": "2025-01-20",
    "text": "Сегодня был отличный день",
    "mood": "happy"
  }'
```

### Получить все записи

```bash
curl http://localhost:8000/entries
```

## Деплой на Railway

Проект готов к деплою на Railway:

1. Подключи репозиторий к Railway
2. Railway автоматически определит команду запуска из `Procfile`
3. Сервис будет доступен на предоставленном Railway URL

Railway автоматически установит все зависимости и запустит сервер.

## Технологии

- FastAPI
- Uvicorn
- Pydantic


