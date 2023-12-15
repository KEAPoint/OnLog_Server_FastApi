from database import Base
from enum import Enum as PyEnum
from sqlalchemy import Enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID
from datetime import datetime


class AccountType(PyEnum):
    DEFAULT = "DEFAULT"
    KAKAO = "KAKAO"


class Role(PyEnum):
    USER = 'user'
    ADMIN = 'admin'


class Blog(Base):
    __tablename__ = "blogs"

    blog_id = Column(GUID, primary_key=True, index=True, unique=True)  # 사용자 블로그 id
    member_idx = Column(Integer)  # 사용자 식별자
    blog_name = Column(String)  # 사용자 블로그 이름
    blog_nickname = Column(String)  # 사용자 블로그 별명 (닉네임)
    blog_profile_img = Column(String, nullable=True)  # 사용자 블로그 프로필
    blog_intro = Column(String, nullable=True)  # 사용자 블로그 한 줄 소개
    blog_theme_img = Column(String, nullable=True)  # 사용자 블로그 테마 이미지

    posts = relationship("Post", back_populates="blog")  # 작성한 게시글
    categories = relationship("Category")  # 사용자 카테고리
    comments = relationship("Comment", back_populates="blog")  # 사용자가 작성한 댓글


class BlogHits(Base):
    __tablename__ = "blog_hits"

    blog_hits_id = Column(GUID, primary_key=True, index=True, unique=True)  # 블로그 방문 식별자
    blog_visit_date = Column(DateTime)  # 날짜
    blog_id = Column(GUID)  # 블로그 식별자
    blog_visitor_count = Column(Integer)  # 블로그 방문자 수


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)  # 카테고리 식별자
    name = Column(String)  # 카테고리 이름
    order = Column(Integer)  # 카테고리 배치 순서

    posts = relationship("Post", back_populates="category")  # 카테고리에 속하는 게시글


class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(GUID, primary_key=True, index=True, unique=True)  # 댓글 식별자
    content = Column(String)  # 댓글 내용
    modified = Column(Boolean)  # 댓글 수정 여부
    ref = Column(Integer)  # 댓글 그룹
    ref_order = Column(Integer)  # 댓글 그룹 순서
    step = Column(Integer)  # 댓글의 계층
    parent_num = Column(GUID, nullable=True)  # 부모 댓글의 ID
    answer_num = Column(Integer)  # 해당 댓글의 자식 댓글의 수
    likes_count = Column(Integer)  # 댓글 좋아요 수

    post_id = Column(GUID, ForeignKey("posts.post_id"))
    post = relationship("Post", back_populates="comments")  # 댓글이 달린 게시글

    blog_id = Column(GUID, ForeignKey("blogs.blog_id"))
    writer = relationship("Blog", back_populates="comments")  # 댓글을 작성한 블로그


class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True, index=True)  # 팔로우 식별자
    blog_id = Column(GUID, ForeignKey("blogs.blog_id"))
    me = relationship("Blog", back_populates="follows", foreign_keys=[blog_id])  # 팔로우 하는 블로그 식별자

    follow_id = Column(GUID, ForeignKey("blogs.blog_id"))
    target = relationship("Blog", back_populates="follows", foreign_keys=[follow_id])  # 팔로우 당하는 블로그 식별자


class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True, index=True)  # 해시태그 식별자
    name = Column(String)  # 해시태그 이름

    post_list = relationship("Post", secondary="post_hashtags")  # 해시태그를 가진 게시글


class Member(Base):
    __tablename__ = "members"

    member_idx = Column(GUID, primary_key=True, index=True, unique=True)  # 사용자 식별자
    email = Column(String)  # 사용자 이메일
    password = Column(String)  # 사용자 비밀번호
    phone_number = Column(String, nullable=True)  # 사용자 휴대폰 번호
    agree_personal_info = Column(Boolean)  # 개인정보 동의 여부
    agree_promotion = Column(Boolean)  # 프로모션 동의 여부
    refresh_token = Column(String, nullable=True)  # refresh token
    role = Column(Enum(Role))  # 역할 (사용자 or 관리자)
    account_type = Column(Enum(AccountType))  # 계정 로그인 정보 (기본 or 카카오)
    user_name = Column(String)  # 사용자 이름

    blog_list = relationship("Blog", back_populates="members")  # 사용자가 가진 블로그


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(GUID, primary_key=True, index=True, unique=True)  # 게시글 식별자
    post_hits = Column(Integer, default=0)  # 게시글 방문 횟수
    title = Column(String)  # 게시글 제목
    content = Column(String, nullable=True)  # 게시글 내용
    summary = Column(String, nullable=True)  # 게시글 요약
    thumbnail_link = Column(String, nullable=True)  # 게시글 썸네일 사진
    is_public = Column(Boolean, default=True)  # 게시글 공개 여부
    modified = Column(Boolean, default=False)  # 게시글 수정 여부
    likes_count = Column(Integer, default=0)  # 게시글 좋아요 개수

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="posts")  # 게시글 카테고리

    topic_id = Column(Integer, ForeignKey("topics.id"))
    topic = relationship("Topic", back_populates="posts")  # 게시글 주제

    hashtags = relationship("Hashtag", secondary="post_hashtags")  # 게시글 해시태그

    comments = relationship("Comment", back_populates="post")
    comments_count = Column(Integer, default=0)  # 게시글 댓글

    blog_id = Column(GUID, ForeignKey("blogs.blog_id"))
    writer = relationship("Blog", back_populates="posts")  # 게시글 작성자


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)  # 주제 식별자
    name = Column(String)  # 주제 이름

    posts = relationship("Post", back_populates="topic")  # 주제에 속한 게시글


class UserCommentLike(Base):
    __tablename__ = "user_comment_likes"

    id = Column(Integer, primary_key=True, index=True)  # 댓글 좋아요 식별자
    blog_id = Column(GUID, ForeignKey("blogs.blog_id"))
    blog = relationship("Blog", back_populates="user_comment_likes", foreign_keys=[blog_id])  # 블로그

    comment_id = Column(GUID, ForeignKey("comments.comment_id"))
    comment = relationship("Comment", back_populates="user_comment_likes", foreign_keys=[comment_id])  # 좋아요 한 댓글


class UserPostLike(Base):
    __tablename__ = "user_post_likes"

    id = Column(Integer, primary_key=True, index=True)  # 게시글 좋아요 식별자
    blog_id = Column(GUID, ForeignKey("blogs.blog_id"))
    blog = relationship("Blog", back_populates="user_post_likes", foreign_keys=[blog_id])  # 블로그

    post_id = Column(GUID, ForeignKey("posts.post_id"))
    post = relationship("Post", back_populates="user_post_likes", foreign_keys=[post_id])  # 좋아요 한 게시글
