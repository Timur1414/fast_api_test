from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import get_db
from models.events import ClassicEvent, Questionnaire
from schemas.events import ClassicEventCreateSchema, QuestionnaireCreateSchema
from validators.events import validate_full_name, validate_group

events = APIRouter()


@events.get('/classic_events/', tags=['ClassicEvents'])
def get_all_events(db: Session = Depends(get_db)):
    query = ClassicEvent.get_all_objects(db)
    return {
        'count': len(query),
        'events': query
    }


@events.post('/classic_events/create/', tags=['ClassicEvents'])
def create_event(data: ClassicEventCreateSchema, db: Session = Depends(get_db)):
    new_event = ClassicEvent.create(db, data)
    return new_event


@events.get('/classic_events/{id}/', tags=['ClassicEvents'])
def get_event(id: int, db: Session = Depends(get_db)):
    event = ClassicEvent.get_by_id(db, id)
    return event


@events.get('/questionnaire/', tags=['ClassicEvents'])
def get_all_questionnaires(db: Session = Depends(get_db)):
    query = Questionnaire.get_all_objects(db)
    return {
        'count': len(query),
        'questionnaires': query
    }


@events.post('/questionnaire/create/', tags=['ClassicEvents'])
def create_questionnaire(data: QuestionnaireCreateSchema, db: Session = Depends(get_db)):
    if not validate_full_name(data.searcher_fio):
        raise HTTPException(status_code=404, detail='Wrong name')
    if not validate_group(data.searcher_bmstu_group):
        raise HTTPException(status_code=404, detail='Wrong group')
    new_questionnaire = Questionnaire.create(db, data)
    return new_questionnaire


@events.get('/questionnaire/{id}/', tags=['ClassicEvents'])
def get_questionnaire(id: int, db: Session = Depends(get_db)):
    questionnaire = Questionnaire.get_by_id(db, id)
    return questionnaire
