from sqlalchemy.orm import Session

import models


def create_user_post_like(db: Session, user_post_like_data: dict):
    db_user_post_like = models.UserPostLike(**user_post_like_data)
    db.add(db_user_post_like)
    db.commit()
    db.refresh(db_user_post_like)
    return db_user_post_like


def get_user_post_like(db: Session, user_post_like_id: int):
    return db.query(models.UserPostLike).filter(models.UserPostLike.id == user_post_like_id).first()


def get_user_post_likes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.UserPostLike).offset(skip).limit(limit).all()


def update_user_post_like(db: Session, user_post_like_id: int, user_post_like_data: dict):
    db_user_post_like = db.query(models.UserPostLike).filter(models.UserPostLike.id == user_post_like_id).first()
    for key, value in user_post_like_data.items():
        setattr(db_user_post_like, key, value)
    db.commit()
    db.refresh(db_user_post_like)
    return db_user_post_like


def delete_user_post_like(db: Session, user_post_like_id: int):
    db_user_post_like = db.query(models.UserPostLike).filter(models.UserPostLike.id == user_post_like_id).first()
    db.delete(db_user_post_like)
    db.commit()
