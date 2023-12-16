from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from typing import Optional, List
from uuid import UUID
from schemas.base import BaseResponse
from schemas.blog import BlogDto, BlogProfileDto, PostCreateBlogReqDto, PutUpdateBlogReqDto
from auth.jwt_handler import extract_blog_id

router_blog = APIRouter()


@router_blog.get("/blog/{blog_id}", tags=["Blog"], summary="블로그 조회", description="블로그를 조회합니다.",
                 response_model=BaseResponse[BlogProfileDto])
async def get_my_profile(blog_id: UUID):
    try:
        # token 추출
        # 블로그 조회
        response_data = {}

        return BaseResponse.on_success(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_blog.post("/blog", tags=["Blog"], summary="블로그 생성", description="새로운 블로그를 생성합니다.",
                  response_model=BaseResponse[BlogDto])
async def create_blog(data: PostCreateBlogReqDto = Body(...)):
    try:
        # token 추출
        # 블로그 조회
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_blog.put("/blog/{blog_id}", tags=["Blog"], summary="블로그 수정", description="사용자 블로그 정보를 수정합니다.",
                 response_model=BaseResponse[BlogDto])
async def update_blog(token: str = Header(..., description="JWT token for authorization"),
                      data: PutUpdateBlogReqDto = Body(...)):
    try:
        # token 추출
        # 블로그 수정
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_blog.delete("/blog/{blog_id}", tags=["Blog"], summary="블로그 탈퇴", description="사용자의 블로그를 탈퇴합니다.",
                    response_model=BaseResponse[None])
async def delete_blog(token: str = Header(..., description="JWT token for authorization")):
    try:
        # token 추출
        # 블로그 탈퇴
        response_data = {}

        return BaseResponse.on_success(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)
