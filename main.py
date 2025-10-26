from fastapi import FastAPI, Body, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Mood Diary API",
    version="1.0.0",
    description="API для стоического дневника настроения",
    docs_url="/docs",
    redoc_url="/redoc"
)

class DiaryEntry(BaseModel):
    id: int
    date: str
    text: str
    mood: str

class EntryResponse(BaseModel):
    entry: DiaryEntry
    stoic_comment: str
    stoic_quote: str

class MoodAnalytics(BaseModel):
    period: str
    data: List[dict]

# Имитация БД
db = []

def generate_stoic_comment(text: str, mood: str) -> tuple[str, str]:
    """Генерирует стоический комментарий и цитату на основе записи"""
    # Здесь будет вызов внешнего LLM сервиса
    # Пока возвращаем заглушки
    stoic_quotes = {
        "happy": "Счастье зависит от нас самих. — Аристотель",
        "sad": "Не то, что происходит с тобой, а то, как ты реагируешь на это, имеет значение. — Эпиктет",
        "angry": "Лучший способ отомстить врагу — не быть похожим на него. — Марк Аврелий",
        "neutral": "Принимай события такими, какие они есть. — Марк Аврелий"
    }
    
    comment = f"Ваше настроение '{mood}' — это естественная часть человеческого опыта. Стоики учили, что наши эмоции не должны управлять нами."
    quote = stoic_quotes.get(mood, "Людям свойственно ошибаться, но только мудрецам свойственно учиться на своих ошибках. — Сенека")
    
    return comment, quote

@app.get(
    "/",
    summary="Информация об API",
    description="Возвращает приветственное сообщение и список доступных endpoints",
    tags=["Информация"]
)
def read_root():
    """Главная страница API"""
    return {
        "message": "Welcome to Stoic Diary API",
        "endpoints": {
            "docs": "/docs",
            "entries": "/entries",
            "analytics": "/analytics/mood"
        }
    }

@app.post(
    "/entries",
    response_model=EntryResponse,
    summary="Добавить запись в дневник",
    description="Добавляет новую запись в дневник и возвращает стоический комментарий и цитату",
    response_description="Возвращает добавленную запись со комментарием и цитатой",
    tags=["Записи"]
)
def add_entry(entry: DiaryEntry):
    """
    Добавляет запись в дневник.
    
    **Параметры:**
    - **id**: уникальный идентификатор записи
    - **date**: дата записи в формате YYYY-MM-DD
    - **text**: текст записи
    - **mood**: настроение (happy, sad, angry, neutral, и т.д.)
    
    **Возвращает:**
    - Запись с добавленным стоическим комментарием и цитатой
    """
    db.append(entry)
    stoic_comment, stoic_quote = generate_stoic_comment(entry.text, entry.mood)
    
    return EntryResponse(
        entry=entry,
        stoic_comment=stoic_comment,
        stoic_quote=stoic_quote
    )

@app.get(
    "/entries",
    response_model=List[DiaryEntry],
    summary="Получить все записи",
    description="Возвращает список всех записей из дневника",
    response_description="Массив всех записей дневника",
    tags=["Записи"]
)
def list_entries():
    """
    Получает все записи из дневника.
    
    **Возвращает:**
    - Список всех записей, отсортированных по дате добавления
    """
    return db

@app.get(
    "/analytics/mood",
    response_model=MoodAnalytics,
    summary="Анализ настроения",
    description="Возвращает динамику настроения за указанный период",
    response_description="Статистика настроения с датами, настроением и темами",
    tags=["Аналитика"]
)
def mood_stats(
    period: str = Query(
        default="week",
        description="Период для анализа (week, month, year)",
        example="week"
    )
):
    """
    Получает статистику по настроению за указанный период.
    
    **Параметры:**
    - **period**: период анализа (week, month, year). По умолчанию "week"
    
    **Возвращает:**
    - Динамику настроения с датами, настроениями и темами
    """
    # Заглушка для аналитики
    # В реальной реализации здесь будет анализ записей из БД
    return MoodAnalytics(
        period=period,
        data=[
            {"date": "2025-10-19", "mood": "happy", "topics": ["love", "friendship"]},
            {"date": "2025-10-20", "mood": "sad", "topics": ["job"]},
        ]
    )

if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
