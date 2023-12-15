from sqlalchemy.orm import Session

import models


####################  Blog  ####################
def create_blog(db: Session, blog_data: dict):
    db_blog = models.Blog(**blog_data)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def get_blog(db: Session, blog_id: str):
    return db.query(models.Blog).filter(models.Blog.blog_id == blog_id).first()


def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def update_blog(db: Session, blog_id: str, blog_data: dict):
    db_blog = db.query(models.Blog).filter(models.Blog.blog_id == blog_id).first()
    for key, value in blog_data.items():
        setattr(db_blog, key, value)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def delete_blog(db: Session, blog_id: str):
    db_blog = db.query(models.Blog).filter(models.Blog.blog_id == blog_id).first()
    db.delete(db_blog)
    db.commit()


####################  Category  ####################
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


####################  Comment  ####################
def create_comment(db: Session, comment_data: dict):
    db_comment = models.Comment(**comment_data)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, comment_id: str):
    return db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()


def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).offset(skip).limit(limit).all()


def update_comment(db: Session, comment_id: str, comment_data: dict):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    for key, value in comment_data.items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: str):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    db.delete(db_comment)
    db.commit()


####################  Follow  ####################
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


####################  Hashtag  ####################
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


####################  Member  ####################
def create_member(db: Session, member_data: dict):
    db_member = models.Member(**member_data)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def get_member(db: Session, member_idx: str):
    return db.query(models.Member).filter(models.Member.member_idx == member_idx).first()


def get_members(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Member).offset(skip).limit(limit).all()


def update_member(db: Session, member_idx: str, member_data: dict):
    db_member = db.query(models.Member).filter(models.Member.member_idx == member_idx).first()
    for key, value in member_data.items():
        setattr(db_member, key, value)
    db.commit()
    db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_idx: str):
    db_member = db.query(models.Member).filter(models.Member.member_idx == member_idx).first()


####################  Post  ####################
def create_post(db: Session, post_data: dict):
    db_post = models.Post(**post_data)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: str):
    return db.query(models.Post).filter(models.Post.post_id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()


def update_post(db: Session, post_id: str, post_data: dict):
    db_post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    for key, value in post_data.items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: str):
    db_post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    db.delete(db_post)
    db.commit()


####################  Topic  ####################
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


####################  UserCommentLike  ####################
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


####################  UserPostLike  ####################
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
