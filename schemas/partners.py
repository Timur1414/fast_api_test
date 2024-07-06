from schemas.base import ImageBaseSchema


class PartnerBaseSchema(ImageBaseSchema):
    title: str
    link: str


class PartnerCreateSchema(PartnerBaseSchema):
    pass


class PartnerSchema(PartnerBaseSchema):
    class Config:
        orm_mode = True
