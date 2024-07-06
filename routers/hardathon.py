from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from models.hardathon import Hardathon, Project
from schemas.hardathon import HardathonCreateSchema, ProjectCreateSchema

hardathons = APIRouter()


@hardathons.get('/hardathons/', tags=['Hardathons'])
def get_all_hardathons(db: Session = Depends(get_db)):
    query = Hardathon.get_all_objects(db)
    return {
        'count': len(query),
        'hardathons': query
    }


@hardathons.get('/hardathons/{id}/', tags=['Hardathons'])
def get_hardathon(id: int, db: Session = Depends(get_db)):
    hardathon = Hardathon.get_by_id(db, id)
    return hardathon


@hardathons.post('/hardathons/create/', tags=['Hardathons'])
def create_hardathon(data: HardathonCreateSchema, db: Session = Depends(get_db)):
    new_hardathon = Hardathon.create(db, data)
    return new_hardathon


@hardathons.get('/projects/', tags=['Hardathons'])
def get_all_projects(db: Session = Depends(get_db)):
    query = Project.get_all_objects(db)
    return {
        'count': len(query),
        'projects': query
    }


@hardathons.get('/projects/{id}/', tags=['Hardathons'])
def get_project(id: int, db: Session = Depends(get_db)):
    project = Project.get_by_id(db, id)
    return project


@hardathons.post('/projects/create/', tags=['Hardathons'])
def create_project(data: ProjectCreateSchema, db: Session = Depends(get_db)):
    new_project = Project.create(db, data)
    return new_project


@hardathons.get('/get_event_partners/{id}/', tags=['Hardathons'])
def get_hardathon_partners(id: int, db: Session = Depends(get_db)):
    partners = Hardathon.get_partners(db, id)
    return {
        'count': len(partners),
        'partners': partners
    }
