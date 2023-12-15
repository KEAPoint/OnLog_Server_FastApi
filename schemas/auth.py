from pydantic import BaseModel, Field
from uuid import UUID


class TokensDto(BaseModel):
    grant_type: str = Field(..., title="token 타입")
    access_token: str = Field(..., title="access token")
    refresh_token: str = Field(..., title="refresh token")


class PostLoginRes(BaseModel):
    member_idx: UUID = Field(..., title="사용자 식별자")
    email: str = Field(..., title="사용자 이메일")
    profile_img_url: str = Field(..., title="사용자 프로필 이미지")
    token_info: TokensDto = Field(..., title="회원가입 성공 여부")


class PostLogoutRes(BaseModel):
    is_success: bool = Field(..., title="회원가입 성공 여부")


class SocialAccountUserInfo(BaseModel):
    user_name: str = Field(..., title="사용자 이름")
    user_email: str = Field(..., title="사용자 이메일")
    profile_img_url: str = Field(..., title="사용자 프로필 이미지")
