from sqlalchemy.orm import Session

import models
from uuid import UUID


def create_blog(db: Session, blog_data: dict):
    db_blog = models.Blog(**blog_data)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def get_blog(db: Session, blog_id: UUID):
    return db.query(models.Blog).filter(models.Blog.blog_id == blog_id).first()


def update_blog(db: Session, blog_id: UUID, blog_data: dict):
    db_blog = db.query(models.Blog).filter(models.Blog.blog_id == blog_id).first()
    for key, value in blog_data.items():
        setattr(db_blog, key, value)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def delete_blog(db: Session, blog_id: UUID):
    db_blog = db.query(models.Blog).filter(models.Blog.blog_id == blog_id).first()
    db.delete(db_blog)
    db.commit()
