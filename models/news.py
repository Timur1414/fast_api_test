from sqlalchemy import String, Column, Text, Integer
from sqlalchemy.orm import Session
from models.base import ImageBaseModel
from schemas.news import NewsCreateSchema


class News(ImageBaseModel):
    __tablename__ = 'News'
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    description = Column(Text())
    new_url = Column(String(100))

    @staticmethod
    def get_all_objects(db: Session, offset: int = 0, limit: int = 100):
        return db.query(News).order_by(News.id.desc()).offset(offset).limit(limit).all()

    @staticmethod
    def create(db: Session, news: NewsCreateSchema):
        new_news = News(
            title=news.title,
            description=news.description,
            new_url=news.new_url,
            photo=news.photo
        )
        db.add(new_news)
        db.commit()
        db.refresh(new_news)
        return new_news