from sqlalchemy.orm import Session

import models


def create_topic(db: Session, topic_data: dict):
    db_topic = models.Topic(**topic_data)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic


def get_topic(db: Session, topic_id: int):
    return db.query(models.Topic).filter(models.Topic.id == topic_id).first()


def get_topics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Topic).offset(skip).limit(limit).all()


def update_topic(db: Session, topic_id: int, topic_data: dict):
    db_topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    for key, value in topic_data.items():
        setattr(db_topic, key, value)
    db.commit()
    db.refresh(db_topic)
    return db_topic


def delete_topic(db: Session, topic_id: int):
    db_topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    db.delete(db_topic)
    db.commit()
