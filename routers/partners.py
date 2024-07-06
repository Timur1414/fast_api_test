from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from models.partners import Partner
from schemas.partners import PartnerCreateSchema

partners = APIRouter()


@partners.get('/', tags=['Partners'])
def get_all_partners(db: Session = Depends(get_db)):
    query = Partner.get_all_objects(db)
    return {
        'count': len(query),
        'partners': query
    }


@partners.post('/create/', tags=['Partners'])
def create_partner(data: PartnerCreateSchema, db: Session = Depends(get_db)):
    new_partner = Partner.create(db, data)
    return new_partner
