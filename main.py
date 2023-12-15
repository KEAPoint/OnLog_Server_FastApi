from fastapi import Depends, FastAPI, HTTPException
from routes.blog import router_blog
from routes.blog_follow import router_blog_follow
from routes.category import router_category
from routes.comment import router_comment
from routes.comment_like import router_comment_like
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


app.include_router(router_blog)
app.include_router(router_blog_follow)
app.include_router(router_category)
app.include_router(router_comment)
app.include_router(router_comment_like)
app.include_router(router_post)
app.include_router(router_post_like)