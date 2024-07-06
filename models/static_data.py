from sqlalchemy import String, Column
from models.database import Base


class StaticData(Base):
    __tablename__ = 'StaticData'
    address = Column(String(150))
    phone = Column(String(10))
    email = Column(String(50))
    link_to_driving_scheme = Column(String(100))
    link_to_vk = Column(String(100))
    link_to_telegram = Column(String(100))
