from sqlalchemy import desc
from sqlalchemy.orm import Session

import models
from uuid import UUID


def create_post(db: Session, post_data: dict):
    db_post = models.Post(**post_data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: UUID):
    return db.query(models.Post).filter(models.Post.post_id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_recent_posts(db: Session, my_blog_id: UUID, topic_name: str, hashtag: str, blog_id: UUID, category_id: int,
                     is_public: bool, page: int, page_size: int):
    query = db.query(models.Post)

    if topic_name:
        query = query.filter(models.Post.topic_name == topic_name)

    if hashtag:
        query = query.filter(models.Post.hashtag == hashtag)

    if blog_id:
        query = query.filter(models.Post.blog_id == blog_id)

    if category_id:
        query = query.filter(models.Post.category_id == category_id)

    if is_public:
        query = query.filter(models.Post.is_public == is_public)

    posts = query.order_by(desc(models.Post.created_at)).offset((page - 1) * page_size).limit(page_size).all()

    return posts


def update_post(db: Session, post_id: UUID, post_data: dict):
    db_post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    for key, value in post_data.items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: UUID):
    db_post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    db.delete(db_post)
    db.commit()
