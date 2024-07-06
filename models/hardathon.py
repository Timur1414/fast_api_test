from sqlalchemy import Column, DateTime, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session
from models.base import EventBaseModel, ImageBaseModel
from schemas.hardathon import HardathonCreateSchema, ProjectCreateSchema


class Hardathon(EventBaseModel):
    __tablename__ = 'Hardathon'
    id = Column(Integer, primary_key=True)
    date_for_accepting_applications = Column(DateTime())
    closing_date_for_applications = Column(DateTime())
    summing_up_date = Column(DateTime())
    main_organizer_photo = Column(String(100))
    main_organizer_word = Column(String(100))
    competition_task = Column(String(100))
    partners = relationship('Partner', back_populates='hardathon')

    @staticmethod
    def get_all_objects(db: Session, offset: int = 0, limit: int = 100):
        return db.query(Hardathon).order_by(Hardathon.id.desc()).offset(offset).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, id: int):
        return db.query(Hardathon).get(id)

    @staticmethod
    def get_partners(db: Session, id: int):
        hardathon = Hardathon.get_by_id(db, id)
        return hardathon.partners

    @staticmethod
    def create(db: Session, hardathon: HardathonCreateSchema):
        new_hardathon = Hardathon(
            date_for_accepting_applications=hardathon.date_for_accepting_applications,
            closing_date_for_applications=hardathon.closing_date_for_applications,
            summing_up_date=hardathon.summing_up_date,
            main_organizer_photo=hardathon.main_organizer_photo,
            main_organizer_word=hardathon.main_organizer_word,
            competition_task=hardathon.competition_task,
            partners=hardathon.partners,
            photo=hardathon.photo
        )
        db.add(new_hardathon)
        db.commit()
        db.refresh(new_hardathon)
        return new_hardathon


class Project(ImageBaseModel):
    __tablename__ = 'Project'
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    description = Column(Text())
    competition_rules = Column(Text())
    implementation_scale = Column(Text())
    hardathon = Column(Integer(), ForeignKey(Hardathon.id), nullable=False)

    @staticmethod
    def get_all_objects(db: Session, offset: int = 0, limit: int = 100):
        return db.query(Project).order_by(Project.id.desc()).offset(offset).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, id: int):
        return db.query(Project).get(id)

    @staticmethod
    def create(db: Session, project: ProjectCreateSchema):
        new_project = Project(
            title=project.title,
            description=project.description,
            competition_rules=project.competition_rules,
            implementation_scale=project.implementation_scale,
            hardathon=project.hardathon,
            photo=project.photo
        )
        db.add(new_project)
        db.commit()
        db.refresh(new_project)
        return new_project
