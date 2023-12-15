from fastapi import Depends, FastAPI, HTTPException
from routes.post import router_post
from routes.post_like import router_post_like

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(router_post)
app.include_router(router_post_like)