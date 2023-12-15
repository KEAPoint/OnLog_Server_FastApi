from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from schemas.base import BaseResponse
from schemas.post_like import PostLikeDto
from auth.jwt_handler import verify_access_token

router_post_like = APIRouter()


@router_post_like.post("/posts/{post_id}/like", tags=["Post"], summary="게시글 좋아요",
                       description="사용자가 특정 게시글에 좋아요를 남깁니다.",
                       response_model=BaseResponse[PostLikeDto])
async def like_post(
        token: str = Header(..., description="JWT token for authorization"),
):
    try:
        # token 추출
        # 게시글 좋아요
        response_data = {}

        return BaseResponse.on_success(response_data)


    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_post_like.delete("/posts/{post_id}/like", tags=["Post"], summary="게시글 좋아요 취소",
                         description="사용자가 특정 게시물에 남긴 좋아요를 취소합니다.",
                         response_model=BaseResponse[PostLikeDto])
async def like_post(
        token: str = Header(..., description="JWT token for authorization"),
):
    try:
        # token 추출
        # 게시글 좋아요 취소
        response_data = {}

        return BaseResponse.on_success(response_data)


    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)
