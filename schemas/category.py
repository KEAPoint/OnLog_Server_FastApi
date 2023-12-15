from pydantic import BaseModel, Field


class CategoryDto(BaseModel):
    id: int = Field(..., title="카테고리 식별자")
    name: str = Field(..., title="카테고리 이름")
    order: int = Field(..., title="카테고리 순서")


class PostCreateCategoryReqDto(BaseModel):
    name: str = Field(..., title="생성할 카테고리 이름")


class PutCategoryUpdateReqDto(BaseModel):
    name: str = Field(..., title="수정할 카테고리 이름")
