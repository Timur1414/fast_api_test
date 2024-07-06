from datetime import datetime
from pydantic import BaseModel


class ImageBaseSchema(BaseModel):
    photo: str


class ImageCreateSchema(ImageBaseSchema):
    pass


class ImageSchema(ImageBaseSchema):
    id: int

    class Config:
        orm_mode = True


class EventBaseSchema(ImageBaseSchema):
    title: str
    description: str
    photo_album_url: str
    documents_url: str
    location: str
    event_date: datetime
    social_media_mention: str


class EventCreateSchema(EventBaseSchema):
    pass


class EventSchema(EventBaseSchema):
    id: int

    class Config:
        orm_mode = True
