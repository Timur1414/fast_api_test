from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import Session
from models.base import ImageBaseModel
from schemas.achievements import AchievementCreateSchema


class Achievement(ImageBaseModel):
    __tablename__ = 'Achievement'
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    description = Column(Text())
    photo_album_url = Column(String(100))
    link_to_media = Column(String(100))

    @staticmethod
    def get_all_objects(db: Session, offset: int = 0, limit: int = 100):
        return db.query(Achievement).order_by(Achievement.id.desc()).offset(offset).limit(limit).all()

    @staticmethod
    def create(db: Session, achievement: AchievementCreateSchema):
        new_achievement = Achievement(
            title=achievement.title,
            description=achievement.description,
            photo_album_url=achievement.photo_album_url,
            link_to_media=achievement.link_to_media,
            photo=achievement.photo
        )
        db.add(new_achievement)
        db.commit()
        db.refresh(new_achievement)
        return new_achievement
