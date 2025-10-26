from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

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

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Stoic Diary API",
        "endpoints": {
            "docs": "/docs",
            "entries": "/entries",
            "analytics": "/analytics/mood"
        }
    }

@app.post("/entries", response_model=EntryResponse)
def add_entry(entry: DiaryEntry):
    db.append(entry)
    stoic_comment, stoic_quote = generate_stoic_comment(entry.text, entry.mood)
    
    return EntryResponse(
        entry=entry,
        stoic_comment=stoic_comment,
        stoic_quote=stoic_quote
    )

@app.get("/entries", response_model=List[DiaryEntry])
def list_entries():
    return db

@app.get("/analytics/mood", response_model=MoodAnalytics)
def mood_stats(period: str = "week"):
    # Заглушка для аналитики
    # В реальной реализации здесь будет анализ записей из БД
    return MoodAnalytics(
        period=period,
        data=[
            {"date": "2025-10-19", "mood": "happy", "topics": ["друзья", "учёба"]},
            {"date": "2025-10-20", "mood": "sad", "topics": ["работа"]},
        ]
    )
