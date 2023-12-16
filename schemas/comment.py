from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from .blog import BlogDto


class CommentDto(BaseModel):
    comment_id: UUID = Field(..., title="댓글 식별자")
    content: str = Field(..., title="댓글 내용")
    modified: bool = Field(..., title="댓글 수정 여부")
    ref: int = Field(..., title="그룹")
    ref_order: int = Field(..., title="그룹 순서")
    step: int = Field(..., title="댓글의 계층")
    parent_comment_id: UUID = Field(..., title="부모 댓글의 ID")
    answer_num: int = Field(..., title="해당 댓글의 자식 댓글의 수")
    created_at: datetime = Field(..., title="댓글 작성 시간")
    post_id: UUID = Field(..., title="댓글이 달린 게시글 식별자")
    writer: BlogDto = Field(..., title="댓글 작성자의 블로그 식별자")
    comment_liked: bool = Field(..., title="댓글 좋아요 하고 있는지 여부")
    likes_count: int = Field(..., title="댓글 좋아요 갯수")


class CommentSummaryDto(BaseModel):
    comment_id: UUID = Field(..., title="댓글 식별자")
    content: str = Field(..., title="댓글 내용")
    modified: bool = Field(..., title="댓글 수정 여부")
    ref: int = Field(..., title="그룹")
    ref_order: int = Field(..., title="그룹 순서")
    step: int = Field(..., title="댓글의 계층")
    parent_comment_id: UUID = Field(..., title="부모 댓글의 ID")
    answer_num: int = Field(..., title="해당 댓글의 자식 댓글의 수")
    created_at: datetime = Field(..., title="댓글 작성 시간")


class PostCreateCommentReqDto(BaseModel):
    content: str = Field(..., title="댓글 내용")
    parent_comment_id: Optional[UUID] = Field(None, title="부모댓글의 ID (null 가능)")

    class Config:
        schema_extra = {
            "example": {
                "content": "저의 겨울 최애 간식은 사실 붕어빵이랍니다 ㅎㅎ",
                "parent_comment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }


class PutUpdateCommentReqDto(BaseModel):
    content: str = Field(..., title="댓글 내용")

    class Config:
        schema_extra = {
            "example": {
                "content": "저의 겨울 최애 간식은 사실 붕어빵이랍니다 ㅎㅎ",
            }
        }
