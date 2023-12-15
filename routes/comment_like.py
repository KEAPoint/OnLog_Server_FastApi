from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from typing import Optional, List
from uuid import UUID
from schemas import BaseResponse, CommentLikeDto
from auth.jwt_handler import verify_access_token

router_comment_like = APIRouter()


@router_comment_like.post("/post/{post_id}/comments/{comment_id}/like", tags=["Comment"], summary="댓글 좋아요",
                          description="사용자가 특정 댓글에 좋아요를 남깁니다.",
                          response_model=BaseResponse[CommentLikeDto])
async def like_comment(
        token: str = Header(..., description="JWT token for authorization"),
):
    try:
        # token 추출
        # 댓글 좋아요
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_comment_like.delete("/post/{post_id}/comments/{comment_id}/like", tags=["Comment"], summary="댓글 좋아요 취소",
                            description="사용자가 특정 댓글에 남긴 좋아요를 취소합니다.",
                            response_model=BaseResponse[CommentLikeDto])
async def unlike_comment(
        token: str = Header(..., description="JWT token for authorization"),
):
    try:
        # token 추출
        # 댓글 좋아요
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)
