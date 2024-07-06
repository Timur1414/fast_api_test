from pydantic import BaseModel
from schemas.base import EventBaseSchema
from schemas.partners import PartnerSchema


class ClassicEventBaseSchema(EventBaseSchema):
    registration_link: str
    partners: list[PartnerSchema] = []


class ClassicEventCreateSchema(ClassicEventBaseSchema):
    pass


class ClassicEventSchema(ClassicEventBaseSchema):
    class Config:
        orm_mode = True


class QuestionnaireBaseSchema(BaseModel):
    searcher_fio: str
    searcher_bmstu_group: str
    participants_count: str
    required_competencies: str
    searcher_VK: str
    additional: str
    classic_event: int


class QuestionnaireCreateSchema(QuestionnaireBaseSchema):
    pass


class QuestionnaireSchema(QuestionnaireBaseSchema):
    class Config:
        orm_mode = True
