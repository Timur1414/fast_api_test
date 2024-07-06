from schemas.base import ImageBaseSchema


class AchievementBaseSchema(ImageBaseSchema):
    title: str
    description: str
    photo_album_url: str
    link_to_media: str


class AchievementCreateSchema(AchievementBaseSchema):
    pass


class AchievementSchema(AchievementBaseSchema):
    class Config:
        orm_mode = True
