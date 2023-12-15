from pydantic import BaseModel, Field


class HashtagDto(BaseModel):
    id: int = Field(..., title="해시태그 식별자")
    name: str = Field(..., title="해시태그 내용")
