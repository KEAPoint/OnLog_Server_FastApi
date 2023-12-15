from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from typing import Optional, List
from uuid import UUID
from schemas.base import BaseResponse
from schemas.category import CategoryDto, PostCreateCategoryReqDto, PutCategoryUpdateReqDto
from auth.jwt_handler import verify_access_token

router_category = APIRouter()


@router_category.get("/blog/{blog_id}/categories", tags=["Blog"], summary="카테고리 조회", description="특정 유저의 카테고리를 조회합니다.",
                     response_model=BaseResponse[List[CategoryDto]])
async def get_categories(blog_id: UUID):
    try:
        # token 추출
        # 카테고리 조회
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_category.post("/blog/{blog_id}/categories", tags=["Blog"], summary="카테고리 생성", description="새로운 카테고리를 생성합니다.",
                      response_model=BaseResponse[CategoryDto])
async def create_category(
        token: str = Header(..., description="JWT token for authorization"),
        dto: PostCreateCategoryReqDto = Body(...)
):
    try:
        # token 추출
        # 카테고리 생성
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_category.put("/blog/{blog_id}/categories/{category_id}", tags=["Blog"], summary="카테고리 수정",
                     description="카테고리 이름을 수정합니다.",
                     response_model=BaseResponse[CategoryDto])
async def update_category(
        token: str = Header(..., description="JWT token for authorization"),
        dto: PutCategoryUpdateReqDto = Body(...)
):
    try:
        # token 추출
        # 카테고리 수정
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_category.delete("/blog/{blog_id}/categories/{category_id}", tags=["Blog"], summary="카테고리 삭제",
                        description="카테고리를 삭제합니다.",
                        response_model=BaseResponse[None])
async def delete_category(token: str = Header(..., description="JWT token for authorization")):
    try:
        # token 추출
        # 카테고리 삭제
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)
