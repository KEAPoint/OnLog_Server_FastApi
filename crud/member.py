from sqlalchemy.orm import Session

import models


def create_member(db: Session, member_data: dict):
    db_member = models.Member(**member_data)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def get_member(db: Session, member_idx: str):
    return db.query(models.Member).filter(models.Member.member_idx == member_idx).first()


def update_member(db: Session, member_idx: str, member_data: dict):
    db_member = db.query(models.Member).filter(models.Member.member_idx == member_idx).first()
    for key, value in member_data.items():
        setattr(db_member, key, value)
    db.commit()
    db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_idx: str):
    db_member = db.query(models.Member).filter(models.Member.member_idx == member_idx).first()
