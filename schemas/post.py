from typing import List
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from .topic import TopicDto
from .category import CategoryDto
from .hashtag import HashtagDto
from .comment import CommentDto
from .blog import BlogDto


class PostDto(BaseModel):
    post_id: UUID = Field(..., title="게시글 식별자")
    post_hits: int = Field(..., title="게시글 방문 횟수")
    title: str = Field(..., title="게시글 제목")
    content: str = Field(..., title="게시글 내용")
    summary: str = Field(..., title="게시글 3줄 요약")
    thumbnail_link: str = Field(..., title="게시글 thumbnail 사진 위치")
    post_liked: bool = Field(..., title="게시글을 좋아요 하고 있는지 여부")
    likes_count: int = Field(..., title="게시글 좋아요 갯수")
    is_public: bool = Field(..., title="게시글 공개 여부")
    is_modified: bool = Field(..., title="게시글 수정 여부")
    topic: TopicDto = Field(..., title="게시글 주제")
    category: CategoryDto = Field(..., title="게시글 카테고리")
    hashtag_list: List[HashtagDto] = Field(..., title="해시태그 리스트")
    comments_counts: int = Field(..., title="게시글 댓글 갯수")
    comments: List[CommentDto] = Field(..., title="게시글 댓글")
    writer: BlogDto = Field(..., title="작성자")
    created_at: datetime = Field(..., title="게시글 생성 시점")


class PostSummaryDto(BaseModel):
    post_id: UUID = Field(..., title="게시글 식별자")
    title: str = Field(..., title="게시글 제목")
    content: str = Field(..., title="게시글 내용")
    summary: str = Field(..., title="게시글 3줄 요약")
    thumbnail_link: str = Field(..., title="게시글 thumbnail 사진 위치")
    likes_count: int = Field(..., title="게시글 좋아요 갯수")
    category: CategoryDto = Field(..., title="게시글 카테고리")
    topic: TopicDto = Field(..., title="게시글 주제")
    comments_counts: int = Field(..., title="게시글 댓글 갯수")
    writer: BlogDto = Field(..., title="작성자")
    created_at: datetime = Field(..., title="게시글 작성 시간")


class PostWithRelatedPostsDto(BaseModel):
    data: PostDto = Field(..., title="사용자가 조회한 게시글")
    related_posts: List[PostSummaryDto] = Field(..., title="같은 카테고리의 다른 게시글들")


class PostWritePostReqDto(BaseModel):
    title: str = Field(..., title="게시글 제목")
    content: str = Field(..., title="게시글 내용")
    summary: str = Field(..., title="게시글 3줄 요약")
    thumbnail_link: str = Field(..., title="게시글 thumbnail 사진 위치")
    is_public: bool = Field(..., title="게시글 공개 여부")
    category_id: int = Field(..., title="게시글 카테고리")
    hashtag_list: List[str] = Field(..., title="게시글 hashtag")
    topic_id: int = Field(..., title="게시글 주제 식별자")


class PutModifyPostReqDto(BaseModel):
    title: str = Field(..., title="게시글 제목")
    content: str = Field(..., title="게시글 내용")
    summary: str = Field(..., title="게시글 3줄 요약")
    thumbnail_link: str = Field(..., title="게시글 thumbnail 사진 위치")
    is_public: bool = Field(..., title="게시글 공개 여부")
    category_id: int = Field(..., title="게시글 카테고리")
    hashtag_list: List[str] = Field(..., title="게시글 hashtag")
    topic_id: int = Field(..., title="게시글 주제 식별자")
