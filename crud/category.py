from sqlalchemy.orm import Session

import models


def create_category(db: Session, category_data: dict):
    db_category = models.Category(**category_data)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()


def update_category(db: Session, category_id: int, category_data: dict):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    for key, value in category_data.items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    db.delete(db_category)
    db.commit()
