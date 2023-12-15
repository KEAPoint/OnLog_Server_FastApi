from pydantic import BaseModel, Field
from uuid import UUID


class PostLikeDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    post_id: UUID = Field(..., title="게시글 식별자")
    is_liked: bool = Field(..., title="사용자가 해당 게시글에 대해 '좋아요' 상태인지 나타내는 플래그")
