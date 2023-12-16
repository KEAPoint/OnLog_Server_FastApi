from fastapi import APIRouter, HTTPException, Header, Body, FastAPI
from uuid import UUID
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from crud.blog import get_blog, create_blog, delete_blog, update_blog
from database import SessionLocal
from models import Blog
from schemas.base import BaseResponse
from schemas.blog import BlogDto, BlogProfileDto, PostCreateBlogReqDto, PutUpdateBlogReqDto

router_blog = APIRouter()


@router_blog.get("/blog/{blog_id}", tags=["Blog"], summary="블로그 조회", description="블로그를 조회합니다.",
                 response_model=BaseResponse[BlogProfileDto])
async def get_my_profile(blog_id: UUID):
    try:
        db: Session = SessionLocal()

        # 블로그 조회
        blog = get_blog(db, blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        return BaseResponse.on_success(BlogProfileDto(blog=blog))

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")


@router_blog.post("/blog", tags=["Blog"], summary="블로그 생성", description="새로운 블로그를 생성합니다.",
                  response_model=BaseResponse[BlogDto])
async def post_create_blog(data: PostCreateBlogReqDto = Body(...)):
    db: Session = SessionLocal()

    # 로깅
    print(f"블로그 생성 요청 정보: {data}")

    # 해당 id를 기반으로 이미 블로그가 있는 경우 예외를 발생시킵니다.
    if get_blog(db, data.blog_id):
        raise HTTPException(status_code=400, detail="이미 블로그가 존재합니다.")

    # 해당 nickname의 블로그가 있는 경우 예외를 발생시킵니다.
    if db.query(Blog).filter(Blog.blog_nickname == data.blog_nickname).first():
        raise HTTPException(status_code=400, detail="이미 해당 닉네임의 블로그가 존재합니다.")

    # 예외가 없는 경우 블로그를 생성합니다.
    blog = create_blog(db, data.dict())

    # 생성 결과를 반환합니다.
    response_data = BlogDto(blog_id=blog.id, blog_nickname=blog.nickname)
    return BaseResponse.on_create(response_data)


@router_blog.put("/blog/{blog_id}", tags=["Blog"], summary="블로그 수정", description="사용자 블로그 정보를 수정합니다.",
                 response_model=BaseResponse[BlogDto])
async def put_update_blog(blog_id: UUID, token: str = Header(..., description="JWT token for authorization"),
                          data: PutUpdateBlogReqDto = Body(...)):
    try:
        db: Session = SessionLocal()

        # 블로그 수정
        blog = get_blog(db, blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        updated_blog = update_blog(db, blog_id, data.dict())

        return BaseResponse.on_success(BlogDto(
            blog_id=updated_blog.blog_id,
            blog_name=updated_blog.blog_name,
            blog_nickname=updated_blog.blog_nickname,
            blog_profile_img=updated_blog.blog_profile_img,
            blog_intro=updated_blog.blog_intro
        ))

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")


@router_blog.delete("/blog/{blog_id}", tags=["Blog"], summary="블로그 탈퇴", description="사용자의 블로그를 탈퇴합니다.",
                    response_model=BaseResponse[None])
async def delete_delete_blog(blog_id: UUID, token: str = Header(..., description="JWT token for authorization")):
    try:
        db: Session = SessionLocal()

        # 블로그 탈퇴
        blog = get_blog(db, blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        delete_blog(db, blog_id)

        return BaseResponse.on_success(None)

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")
