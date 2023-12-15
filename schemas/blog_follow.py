from pydantic import BaseModel, Field
from uuid import UUID


class BlogFollowDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    follow_id: UUID = Field(..., title="팔로우 블로그 식별자")
    is_following: bool = Field(..., title="해당 블로그를 팔로잉 하고 있는지 여부")
