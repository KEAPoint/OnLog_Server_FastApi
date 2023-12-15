from pydantic import BaseModel, Field


class TopicDto(BaseModel):
    id: int = Field(..., title="주제 식별자")
    name: str = Field(..., title="주제 이름")
