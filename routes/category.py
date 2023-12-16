from fastapi import APIRouter, HTTPException, Header, Body, FastAPI
from typing import List
from uuid import UUID
from fastapi.encoders import jsonable_encoder
from models import Category
from schemas.base import BaseResponse
from schemas.category import CategoryDto, PostCreateCategoryReqDto, PutCategoryUpdateReqDto
from crud.blog import get_blog
from crud.category import get_categories, create_category, delete_category, update_category
from sqlalchemy.orm import Session
from database import SessionLocal
from loguru import logger
from datetime import datetime

router_category = APIRouter()


@router_category.get("/blog/{blog_id}/categories", tags=["Blog"], summary="카테고리 조회", description="특정 유저의 카테고리를 조회합니다.",
                     response_model=BaseResponse[List[CategoryDto]])
async def get_categories(blog_id: UUID):
    try:
        db: Session = SessionLocal()

        # 블로그 조회
        blog = get_blog(db, blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        logger.info("카테고리 조회할 블로그 정보: {blog}")

        # 유효한 카테고리만 반환
        categories = get_categories(db, blog_id, 0, 10)
        return BaseResponse.on_success(jsonable_encoder([CategoryDto(**category.dict()) for category in categories]))

    except HTTPException as e:
        logger.error(e.detail)
        raise e

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")


@router_category.post("/blog/{blog_id}/categories", tags=["Blog"], summary="카테고리 생성", description="새로운 카테고리를 생성합니다.",
                      response_model=BaseResponse[CategoryDto])
async def post_create_category(
        blog_id: UUID,
        token: str = Header(..., description="JWT token for authorization"),
        dto: PostCreateCategoryReqDto = Body(...)
):
    try:
        db: Session = SessionLocal()

        # 블로그 조회
        blog = get_blog(db, blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        logger.info("카테고리 조회할 블로그 정보: {blog}")

        # 사용자가 해당 이름으로 카테고리를 만든 적 있는지 조회
        existing_category = next((category for category in blog.categories if category.name == dto.name), None)

        if existing_category is not None:  # 이미 사용자가 해당 이름으로 카테고리를 가지고 있는 경우 활성화
            existing_category.status = True
            existing_category.created_at = datetime.now()
            new_or_updated_category = existing_category

        else:  # 사용자가 해당 이름으로 카테고리를 만든 적 없는 경우 새로 생성
            category_data = Category(
                name=dto.name,
                order=len(blog.categories) + 1,  # 생성된 카테고리 순서는 가장 마지막
                posts=[]
            )
            new_or_updated_category = create_category(db, category_data)

        # 카테고리 생성
        blog.categories.append(new_or_updated_category)

        logger.info(f"생성된 카테고리 정보: {new_or_updated_category}")

        return BaseResponse.on_create(CategoryDto(**new_or_updated_category.dict()))

    except HTTPException as e:
        logger.error(e.detail)
        return BaseResponse.from_exception(e)

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")


@router_category.put("/blog/{blog_id}/categories/{category_id}", tags=["Blog"], summary="카테고리 수정",
                     description="카테고리 이름을 수정합니다.",
                     response_model=BaseResponse[CategoryDto])
async def update_category(
        blog_id: UUID, category_id: int,
        token: str = Header(..., description="JWT token for authorization"),
        dto: PutCategoryUpdateReqDto = Body(...)
):
    try:
        db: Session = SessionLocal()

        # 블로그 조회
        blog = get_blog(db, blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        logger.info(f"카테고리 수정할 블로그 정보: {blog}")

        # 카테고리 조회
        category = db.query(Category).filter(Category.id == category_id).first()
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")

        logger.info(f"수정할 카테고리 정보: {category}")

        # 사용자가 해당 카테고리를 가지고 있는지 조회
        if category not in blog.categories:
            raise HTTPException(status_code=403, detail="Unauthorized category access")

        # 카테고리 이름 수정
        category_data = {"name": dto.name}
        updated_category = update_category(db, category_id, category_data)
        logger.info(f"수정된 카테고리 정보: {updated_category}")

        # 수정된 카테고리 반환
        return BaseResponse.on_success(CategoryDto(**updated_category.dict()))

    except HTTPException as e:
        logger.error(e.detail)
        return BaseResponse.from_exception(e)

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")


@router_category.delete("/blog/{blog_id}/categories/{category_id}", tags=["Blog"], summary="카테고리 삭제",
                        description="카테고리를 삭제합니다.",
                        response_model=BaseResponse[None])
async def delete_delete_category(blog_id: UUID, category_id: int,
                                 token: str = Header(..., description="JWT token for authorization")):
    try:
        db: Session = SessionLocal()

        # 블로그 조회
        blog = get_blog(db, blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        logger.info(f"카테고리 삭제할 블로그 정보: {blog}")

        # 카테고리 조회
        category = db.query(Category).filter(Category.id == category_id).first()
        if category is None:
            raise HTTPException(status_code=404, detail="Category not found")

        logger.info(f"삭제할 카테고리 정보: {category}")

        # 사용자가 해당 카테고리를 가지고 있는지 조회
        if category not in blog.categories:
            raise HTTPException(status_code=403, detail="Unauthorized category access")

        # 해당 카테고리에 속한 게시글의 카테고리를 null로 설정
        for post in category.posts:
            post.category_id = None

        # 카테고리 삭제
        delete_category(db, category_id)
        logger.info("카테고리가 삭제되었습니다.")
        return BaseResponse.on_success(None)

    except HTTPException as e:
        logger.error(e.detail)
        return BaseResponse.from_exception(e)

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")
