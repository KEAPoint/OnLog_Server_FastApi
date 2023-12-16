from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session

from crud.blog import get_blog
from crud.follow import get_follow
from database import SessionLocal
from models import Follow
from schemas.base import BaseResponse
from schemas.blog_follow import BlogFollowDto
from auth.jwt_handler import extract_blog_id

router_blog_follow = APIRouter()


@router_blog_follow.get("/blog/{blog_id}/follow", tags=["Blog"], summary="팔로우 조회",
                        description="내가 팔로우 하고 있는 블로그를 조회합니다.",
                        response_model=BaseResponse[List[BlogFollowDto]])
async def get_get_follow(blog_id: UUID, token: str = Header(..., description="JWT token for authorization")):
    try:
        db: Session = SessionLocal()

        # 내가 팔로우 중인 블로그 조회
        blog = get_blog(db, blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        followers = db.query(Follow).filter(Follow.me == blog).all()

        # followers = get_follow.all()
        if followers is None:
            followers = []

        return BaseResponse.on_success([BlogFollowDto(get_follow(db, follower.id)) for follower in followers])


    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_blog_follow.post("/follow/{blog_id}", tags=["Blog"], summary="팔로우 설정", description="특정 블로그를 팔로우합니다.",
                         response_model=BaseResponse[BlogFollowDto])
async def post_follow(token: str = Header(..., description="JWT token for authorization")):
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
async def delete_unfollow(token: str = Header(..., description="JWT token for authorization")):
    try:
        # token 추출
        # 블로그 팔로우 취소
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)
