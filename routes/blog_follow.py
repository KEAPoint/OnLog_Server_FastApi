from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from typing import Optional, List
from uuid import UUID
from schemas import BaseResponse, BlogFollowDto
from auth.jwt_handler import verify_access_token

router_blog_follow = APIRouter()


@router_blog_follow.get("/blog/{blog_id}/follow", tags=["Blog"], summary="팔로우 조회",
                        description="내가 팔로우 하고 있는 블로그를 조회합니다.",
                        response_model=BaseResponse[List[BlogFollowDto]])
async def follow(token: str = Header(..., description="JWT token for authorization")):
    try:
        # token 추출
        # 내가 팔로우 중인 블로그 조회
        response_data = {}

        return BaseResponse.on_success(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_blog_follow.post("/follow/{blog_id}", tags=["Blog"], summary="팔로우 설정", description="특정 블로그를 팔로우합니다.",
                         response_model=BaseResponse[BlogFollowDto])
async def follow(token: str = Header(..., description="JWT token for authorization")):
    try:
        # token 추출
        # 블로그 팔로우
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_blog_follow.delete("/follow/{blog_id}", tags=["Blog"], summary="팔로우 해제", description="특정 블로그를 팔로우 취소합니다.",
                           response_model=BaseResponse[BlogFollowDto])
async def unfollow(token: str = Header(..., description="JWT token for authorization")):
    try:
        # token 추출
        # 블로그 팔로우 취소
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)
