from fastapi import FastAPI
from routers.achievements import achievements
from models.database import engine, Base
from routers.events import events
from routers.hardathon import hardathons
from routers.news import news
from routers.partners import partners

app = FastAPI()
Base.metadata.create_all(engine)


@app.get('/', tags=['Main'])
def main():
    return {'main': 'page'}


app.include_router(achievements, prefix='/api/v0/achievements')
app.include_router(events, prefix='/api/v0')
app.include_router(hardathons, prefix='/api/v0')
app.include_router(news, prefix='/api/v0/news')
app.include_router(partners, prefix='/api/v0/partners')
