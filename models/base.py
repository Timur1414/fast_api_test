from sqlalchemy import Column, String, Text, DateTime
from models.database import Base


class ImageBaseModel(Base):
    __abstract__ = True
    photo = Column(String(100))

    def __str__(self):
        return self.title


class EventBaseModel(ImageBaseModel):
    __abstract__ = True
    title = Column(String(150))
    description = Column(Text())
    photo_album_url = Column(String(100))
    documents_url = Column(String(100))
    location = Column(String(100))
    event_date = Column(DateTime())
    social_media_mention = Column(String())
