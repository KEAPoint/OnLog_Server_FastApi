from sqlalchemy.orm import Session

import models
from uuid import UUID


def create_comment(db: Session, comment_data: dict):
    db_comment = models.Comment(**comment_data)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, comment_id: UUID):
    return db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()


def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).offset(skip).limit(limit).all()


def update_comment(db: Session, comment_id: UUID, comment_data: dict):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    for key, value in comment_data.items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: UUID):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    db.delete(db_comment)
    db.commit()
