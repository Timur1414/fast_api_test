from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session
from models.base import ImageBaseModel


class Director(ImageBaseModel):
    __tablename__ = 'Director'
    id = Column(Integer, primary_key=True)
    fio = Column(String(150))
    email = Column(String(100))
    role = Column(String(150))

    @staticmethod
    def get_all_objects(db: Session, offset: int = 0, limit: int = 100):
        return db.query(Director).order_by(Director.id.desc()).offset(offset).limit(limit).all()

    def __str__(self):
        return self.fio
