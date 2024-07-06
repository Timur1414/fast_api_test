from sqlalchemy import String, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship, Session
from models.base import EventBaseModel
from models.database import Base
from schemas.events import ClassicEventCreateSchema, QuestionnaireCreateSchema


class ClassicEvent(EventBaseModel):
    __tablename__ = 'ClassicEvent'
    id = Column(Integer, primary_key=True)
    registration_link = Column(String(100))
    partners = relationship('Partner', back_populates='classic_event')

    @staticmethod
    def get_all_objects(db: Session, offset: int = 0, limit: int = 100):
        return db.query(ClassicEvent).order_by(ClassicEvent.id.desc()).offset(offset).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, id: int):
        return db.query(ClassicEvent).get(id)

    @staticmethod
    def create(db: Session, event: ClassicEventCreateSchema):

        new_event = ClassicEvent(
            registration_link=event.registration_link,
            partners=event.partners,
            title=event.title,
            description=event.description,
            photo_album_url=event.photo_album_url,
            documents_url=event.documents_url,
            location=event.location,
            event_date=event.event_date,
            social_media_mention=event.social_media_mention,
            photo=event.photo
        )
        db.add(new_event)
        db.commit()
        db.refresh(new_event)
        return new_event


class Questionnaire(Base):
    __tablename__ = 'Questionnaire'
    id = Column(Integer, primary_key=True)
    searcher_fio = Column(String(150))
    searcher_bmstu_group = Column(String(15))
    participants_count = Column(Integer())
    required_competencies = Column(Text())
    searcher_VK = Column(String(100))
    additional = Column(Text())
    classic_event = Column(Integer, ForeignKey(ClassicEvent.id), nullable=False)

    @staticmethod
    def get_all_objects(db: Session, offset: int = 0, limit: int = 100):
        return db.query(Questionnaire).order_by(Questionnaire.id.desc()).offset(offset).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, id: int):
        return db.query(Questionnaire).get(id)

    @staticmethod
    def create(db: Session, questionnaire: QuestionnaireCreateSchema):
        new_questionnaire = Questionnaire(
            searcher_fio=questionnaire.searcher_fio,
            searcher_bmstu_group=questionnaire.searcher_bmstu_group,
            participants_count=questionnaire.participants_count,
            required_competencies=questionnaire.required_competencies,
            searcher_VK=questionnaire.searcher_VK,
            additional=questionnaire.additional,
            classic_event=questionnaire.classic_event
        )
        db.add(new_questionnaire)
        db.commit()
        db.refresh(new_questionnaire)
        return new_questionnaire

    def __str__(self):
        return self.searcher_fio
