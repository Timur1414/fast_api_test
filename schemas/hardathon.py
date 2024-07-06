from datetime import datetime
from schemas.base import ImageBaseSchema
from schemas.partners import PartnerSchema


class HardathonBaseSchema(ImageBaseSchema):
    date_for_accepting_applications: datetime
    closing_date_for_applications: datetime
    summing_up_date: datetime
    main_organizer_photo: str
    main_organizer_word: str
    competition_task: str
    partners: list[PartnerSchema] = []


class HardathonCreateSchema(HardathonBaseSchema):
    pass


class HardathonSchema(HardathonBaseSchema):
    class Config:
        orm_mode = True


class ProjectBaseSchema(ImageBaseSchema):
    title: str
    description: str
    competition_rules: str
    implementation_scale: str
    hardathon: int


class ProjectCreateSchema(ProjectBaseSchema):
    pass


class ProjectSchema(ProjectBaseSchema):
    class Config:
        orm_mode = True
