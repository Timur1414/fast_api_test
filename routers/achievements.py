from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models.achievements
from models.achievements import Achievement
from models.database import get_db
from schemas.achievements import AchievementCreateSchema

achievements = APIRouter()


@achievements.get('/', tags=['Achievements'])
def get_all_achievements(db: Session = Depends(get_db)):
    query = Achievement.get_all_objects(db)
    return {
        'count': len(query),
        'data': query
    }


@achievements.post('/create/', tags=['Achievements'])
def create_achievement(data: AchievementCreateSchema, db: Session = Depends(get_db)):
    new_achievement = models.achievements.Achievement.create(db, data)
    return new_achievement
