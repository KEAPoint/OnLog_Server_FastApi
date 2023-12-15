from sqlalchemy.orm import Session

import models


def create_follow(db: Session, follow_data: dict):
    db_follow = models.Follow(**follow_data)
    db.add(db_follow)
    db.commit()
    db.refresh(db_follow)
    return db_follow


def get_follow(db: Session, follow_id: int):
    return db.query(models.Follow).filter(models.Follow.id == follow_id).first()


def get_follows(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Follow).offset(skip).limit(limit).all()


def update_follow(db: Session, follow_id: int, follow_data: dict):
    db_follow = db.query(models.Follow).filter(models.Follow.id == follow_id).first()
    for key, value in follow_data.items():
        setattr(db_follow, key, value)
    db.commit()
    db.refresh(db_follow)
    return db_follow


def delete_follow(db: Session, follow_id: int):
    db_follow = db.query(models.Follow).filter(models.Follow.id == follow_id).first()
    db.delete(db_follow)
    db.commit()
