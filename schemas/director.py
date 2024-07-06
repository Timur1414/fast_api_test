from schemas.base import ImageBaseSchema


class DirectorBaseSchema(ImageBaseSchema):
    fio: str
    email: str
    role: str


class DirectorCreateSchema(DirectorBaseSchema):
    pass


class DirectorSchema(DirectorBaseSchema):
    class Config:
        orm_mode = True
