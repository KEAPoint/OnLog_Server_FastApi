from pydantic import BaseModel, Field
from uuid import UUID


class BlogDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    blog_name: str = Field(..., title="블로그 이름")
    blog_nickname: str = Field(..., title="블로그 별명")
    blog_profile_img: str = Field(..., title="블로그 프로필")
    blog_intro: str = Field(..., title="블로그 한 줄 소개")
    blog_theme_img: str = Field(..., title="블로그 테마 이미지")


class BlogProfileDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    blog_name: str = Field(..., title="블로그 이름")
    blog_nickname: str = Field(..., title="블로그 별명")
    blog_profile_img: str = Field(..., title="블로그 프로필")
    blog_intro: str = Field(..., title="블로그 한 줄 소개")
    blog_theme_img: str = Field(..., title="블로그 테마 이미지")
    post_count: int = Field(..., title="작성한 글 개수")
    like_count: int = Field(..., title="좋아요 받은 개수")
    subscriber_count: int = Field(..., title="구독자 수")


class PostCreateBlogReqDto(BaseModel):
    blog_name: str = Field(..., title="블로그 이름")
    blog_nickname: str = Field(..., title="블로그 별명")
    blog_profile_img: str = Field(..., title="블로그 프로필")
    blog_intro: str = Field(..., title="블로그 한 줄 소개")

    class Config:
        schema_extra = {
            "example": {
                "blog_name": "멋쟁이 개미해적단",
                "blog_nickname": "개미1",
                "blog_profile_img": "https://kea-004-s3.s3.amazonaws.com/profile.png",
                "blog_intro": "열심히 살고있는 개미입니다. 모이면 해적단이 됩니다."
            }
        }


class PutUpdateBlogReqDto(BaseModel):
    blog_name: str = Field(..., title="블로그 이름")
    blog_nickname: str = Field(..., title="블로그 별명")
    blog_profile_img: str = Field(..., title="블로그 프로필")
    blog_intro: str = Field(..., title="블로그 한 줄 소개")

    class Config:
        schema_extra = {
            "example": {
                "blog_name": "성남 멋쟁이 개미해적단",
                "blog_nickname": "성남개미",
                "blog_profile_img": "https://kea-004-s3.s3.amazonaws.com/profile.png",
                "blog_intro": "열심히 살고있는 개미입니다. 다같이 모이면 성남해적단이 됩니다."
            }
        }
