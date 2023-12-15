from sqlalchemy.orm import Session

import models


def create_hashtag(db: Session, hashtag_data: dict):
    db_hashtag = models.Hashtag(**hashtag_data)
    db.add(db_hashtag)
    db.commit()
    db.refresh(db_hashtag)
    return db_hashtag


def get_hashtag(db: Session, hashtag_id: int):
    return db.query(models.Hashtag).filter(models.Hashtag.id == hashtag_id).first()


def get_hashtags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Hashtag).offset(skip).limit(limit).all()


def update_hashtag(db: Session, hashtag_id: int, hashtag_data: dict):
    db_hashtag = db.query(models.Hashtag).filter(models.Hashtag.id == hashtag_id).first()
    for key, value in hashtag_data.items():
        setattr(db_hashtag, key, value)
    db.commit()
    db.refresh(db_hashtag)
    return db_hashtag


def delete_hashtag(db: Session, hashtag_id: int):
    db_hashtag = db.query(models.Hashtag).filter(models.Hashtag.id == hashtag_id).first()
    db.delete(db_hashtag)
    db.commit()
