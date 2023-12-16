from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from sqlalchemy.orm import Session
from schemas.base import BaseResponse
from schemas.post_like import PostLikeDto
from auth.jwt_handler import extract_blog_id
from database import get_db
from crud.user_post_like import toggle_like

router_post_like = APIRouter()


@router_post_like.post("/posts/{post_id}/like", tags=["Post"], summary="게시글 좋아요",
                       description="사용자가 특정 게시글에 좋아요를 남깁니다.",
                       response_model=BaseResponse[PostLikeDto])
async def like_post(
        post_id: int,
        token: str = Header(..., description="JWT token for authorization"),
        db: Session = Depends(get_db)
):
    try:
        # JWT 토큰 검증 및 사용자 정보 가져오기
        blog_id = extract_blog_id(token)

        # 게시글 좋아요
        response_data = toggle_like(db, blog_id, post_id)

        # 응답
        return BaseResponse.on_create(response_data)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_post_like.delete("/posts/{post_id}/like", tags=["Post"], summary="게시글 좋아요 취소",
                         description="사용자가 특정 게시물에 남긴 좋아요를 취소합니다.",
                         response_model=BaseResponse[PostLikeDto])
async def like_post(
        post_id: int,
        token: str = Header(..., description="JWT token for authorization"),
        db: Session = Depends(get_db)
):
    try:
        # JWT 토큰 검증 및 사용자 정보 가져오기
        blog_id = extract_blog_id(token)

        # 게시글 좋아요 취소
        response_data = toggle_like(db, blog_id, post_id)

        # 응답
        return BaseResponse.on_create(response_data)

    except Exception as e:
        return BaseResponse.from_exception(e)
