from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session
from models.base import ImageBaseModel
from schemas.partners import PartnerCreateSchema


class Partner(ImageBaseModel):
    __tablename__ = 'Partners'
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    link = Column(String(100))
    hardathon = relationship('Hardathon', back_populates='partners')
    hardathon_id = Column(Integer, ForeignKey('Hardathon.id'))
    classic_event = relationship('ClassicEvent', back_populates='partners')
    classic_event_id = Column(Integer, ForeignKey('ClassicEvent.id'))

    @staticmethod
    def get_all_objects(db: Session, offset: int = 0, limit: int = 100):
        return db.query(Partner).order_by(Partner.id.desc()).offset(offset).limit(limit).all()

    @staticmethod
    def create(db: Session, partner: PartnerCreateSchema):
        new_partner = Partner(
            title=partner.title,
            link=partner.link,
            photo=partner.photo
        )
        db.add(new_partner)
        db.commit()
        db.refresh(new_partner)
        return new_partner
