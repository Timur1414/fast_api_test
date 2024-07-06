from schemas.base import ImageBaseSchema


class NewsBaseSchema(ImageBaseSchema):
    title: str
    description: str
    new_url: str


class NewsCreateSchema(NewsBaseSchema):
    pass


class NewsSchema(NewsBaseSchema):
    class Config:
        orm_mode = True
