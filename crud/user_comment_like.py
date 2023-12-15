from sqlalchemy.orm import Session

import models


def create_user_comment_like(db: Session, user_comment_like_data: dict):
    db_user_comment_like = models.UserCommentLike(**user_comment_like_data)
    db.add(db_user_comment_like)
    db.commit()
    db.refresh(db_user_comment_like)
    return db_user_comment_like


def get_user_comment_like(db: Session, user_comment_like_id: int):
    return db.query(models.UserCommentLike).filter(models.UserCommentLike.id == user_comment_like_id).first()


def get_user_comment_likes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.UserCommentLike).offset(skip).limit(limit).all()


def update_user_comment_like(db: Session, user_comment_like_id: int, user_comment_like_data: dict):
    db_user_comment_like = db.query(models.UserCommentLike).filter(
        models.UserCommentLike.id == user_comment_like_id).first()
    for key, value in user_comment_like_data.items():
        setattr(db_user_comment_like, key, value)
    db.commit()
    db.refresh(db_user_comment_like)
    return db_user_comment_like


def delete_user_comment_like(db: Session, user_comment_like_id: int):
    db_user_comment_like = db.query(models.UserCommentLike).filter(
        models.UserCommentLike.id == user_comment_like_id).first()
    db.delete(db_user_comment_like)
    db.commit()
