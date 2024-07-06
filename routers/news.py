from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from models.news import News
from schemas.news import NewsCreateSchema

news = APIRouter()


@news.get('/', tags=['News'])
def get_all_news(db: Session = Depends(get_db)):
    query = News.get_all_objects(db)
    return {
        'count': len(query),
        'news': query
    }


@news.post('/create/', tags=['News'])
def create_news(data: NewsCreateSchema, db: Session = Depends(get_db)):
    new_news = News.create(db, data)
    return new_news
