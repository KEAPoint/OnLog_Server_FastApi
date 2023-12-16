from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body, Path
from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session
from crud.post import delete_post, get_post, update_post, create_post, get_recent_posts
from crud.user_post_like import delete_user_post_like
from crud.blog import get_blog
from crud.category import get_category
from crud.topic import get_topic
from crud.hashtag import get_hashtags, create_hashtag
from database import SessionLocal
from models import UserPostLike, UserCommentLike
from schemas.base import BaseResponse
from schemas.blog import BlogDto
from schemas.comment import CommentDto
from schemas.post import PostSummaryDto, PostWithRelatedPostsDto, PostWritePostReqDto, PutModifyPostReqDto, PostDto
from auth.jwt_handler import extract_blog_id

router_post = APIRouter()


class Pageable:
    def __init__(self, page: int = Query(1, description="Page number, default is 1", ge=1),
                 size: int = Query(10, description="Items per page, default is 10", ge=1)):
        self.page = page
        self.size = size


@router_post.get("/posts", tags=["Post"], summary="최근 게시글 조회(카드형)", description="조건에 따른 게시글을 조회합니다.(여러개)",
                 response_model=BaseResponse[List[PostSummaryDto]])
async def get_posts(
        token: str = Header(..., description="JWT token for authorization"),
        topic_name: Optional[str] = Query(None),
        hashtag: Optional[str] = Query(None),
        blog_id: Optional[UUID] = Query(None),
        category_id: Optional[int] = Query(None),
        is_public: Optional[bool] = Query(None),
        pageable: Pageable = Depends(Pageable),
):
    try:
        db: Session = SessionLocal()

        my_blog_id = UUID(extract_blog_id(token))

        posts = get_recent_posts(db, my_blog_id, topic_name, hashtag, blog_id, category_id, is_public, pageable.page,
                                 pageable.size)

        return BaseResponse.on_success([PostSummaryDto(**post.dict()) for post in posts])

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")


@router_post.get("/posts/{post_id}", tags=["Post"], summary="특정 게시글 조회", description="게시글 ID에 따른 게시글 상세내용을 조회합니다.(1개)",
                 response_model=BaseResponse[PostWithRelatedPostsDto])
async def get_get_post(
        post_id: UUID = Path(..., description="Post Id"),
        token: str = Header(..., description="JWT token for authorization"),
):
    db: Session = SessionLocal()
    try:
        # 내 블로그를 조회한다.
        blog_id: UUID = extract_blog_id(token)
        me = get_blog(db, blog_id)

        # 게시글을 조회한다.
        post = get_post(db, post_id)

        # 게시글이 삭제되었는지 확인한다.
        if post.status == False:
            raise HTTPException(status_code=404, detail="Post not found")

        # 게시글의 권한을 확인한다.
        if post.is_public == False and post.writer != me:
            raise HTTPException(status_code=403, detail="Access denied")
        post.hit += 1

        # 내가 해당 게시글을 좋아요 하고 있는지 조회한다.
        is_post_liked = db.query(UserPostLike).filter(
            UserPostLike.blog_id == me.blog_id,
            UserPostLike.post_id == post.post_id
        ).first() is not None

        # 댓글 정보
        comment_dto_list = []
        valid_comments = [comment for comment in post.comments if comment.status]
        if valid_comments:
            user_comment_likes = db.query(UserCommentLike).filter(
                UserCommentLike.blog_id == me.blog_id,
                UserCommentLike.comment_id.in_([comment.comment_id for comment in valid_comments])
            ).all()
            comment_dto_list = [
                CommentDto(
                    comment_id=comment.comment_id,
                    content=comment.content,
                    modified=comment.modified,
                    ref=comment.ref,
                    ref_order=comment.ref_order,
                    step=comment.step,
                    parent_comment_id=comment.parent_comment_id,
                    answer_num=comment.answer_num,
                    created_at=comment.created_at,
                    post_id=comment.post_id,
                    writer=BlogDto(**comment.writer.dict()),
                    comment_liked=comment in user_comment_likes,
                    likes_count=comment.likes_count
                ) for comment in valid_comments
            ]
            return BaseResponse.on_success(PostDto(data=PostDto(**post.dict())))

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")


@router_post.post("/posts", tags=["Post"], summary="게시글 작성", description="게시글을 작성합니다.",
                  response_model=BaseResponse[PostSummaryDto])
async def write_post(
        token: str = Header(..., description="JWT token for authorization"),
        dto: PostWritePostReqDto = Body(...),
):
    try:
        db: Session = SessionLocal()

        # 게시글을 작성하고자 하는 사용자를 조회한다.
        blog_id: UUID = extract_blog_id(token)
        writer = get_blog(db, blog_id)

        # 카테고리를 조회한다.
        category = get_category(db, dto.category_id)

        # 해당 카테고리 주인인지 확인한다.
        if category not in writer.categories:
            raise HTTPException(status_code=403, detail="Unauthorized category access")

        # 주제를 조회한다.
        topic = get_topic(db, dto.topic_id)

        # 해시태그를 조회한다. 만약 해시태그가 없는 경우엔 만든다
        hashtag_list = []
        existing_hashtags = get_hashtags(db)
        for hashtag in dto.hashtag_list:
            existing_hashtag = next((h for h in existing_hashtags if h.name == hashtag), None)
            if existing_hashtag is None:
                new_hashtag_data = {"name": hashtag}
                existing_hashtag = create_hashtag(db, new_hashtag_data)
            hashtag_list.append(existing_hashtag)

        # 게시글을 생성한다.
        post_data = {"writer": writer, "category": category, "topic": topic, "hashtag_list": hashtag_list}
        post = create_post(db, post_data)
        result = PostSummaryDto(**post.dict())
        return BaseResponse.on_create(result)

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")


@router_post.put("/posts/{post_id}", tags=["Post"], summary="게시글 수정", description="게시글을 수정합니다.",
                 response_model=BaseResponse[PostSummaryDto])
async def put_update_post(
        post_id: UUID,
        token: str = Header(..., description="JWT token for authorization"),
        dto: PutModifyPostReqDto = Body(...),
):
    try:
        db: Session = SessionLocal()
        writer = UUID(extract_blog_id(token))  # 게시글을 수정하고자 하는 사용자

        # blog_id = jwtTokenProvider.extract_idx(token)  # JWT 토큰에서 사용자 ID 추출 후 UUID로 변환

        # 수정하고자 하는 게시글을 조회
        post = get_post(db, post_id)

        # 게시글이 삭제되었는지 확인
        if post.status == False:
            raise HTTPException(status_code=404, detail="Post not found")

        # 게시글 작성자인지 확인
        if post.writer != writer:
            raise HTTPException(status_code=403, detail="Permission denied")

        # 카테고리를 조회
        category = get_category(db, dto.category_id)

        # 해당 카테고리 주인인지 확인
        if category not in writer.categories:
            raise HTTPException(status_code=403, detail="Unauthorized category access")

        # 주제를 조회
        topic = get_topic(db, dto.topic_id)

        # 해시태그를 조회한다. 만약 해시태그가 없는 경우엔 만든다
        hashtag_list = []
        existing_hashtags = get_hashtags(db)
        for hashtag in dto.hashtag_list:
            existing_hashtag = next((h for h in existing_hashtags if h.name == hashtag.name), None)
            if existing_hashtag is None:
                new_hashtag_data = {"name": hashtag.name}
                existing_hashtag = create_hashtag(db, new_hashtag_data)
            hashtag_list.append(existing_hashtag)

        # 게시글을 수정
        post_data = {"dto": dto, "category": category, "topic": topic, "hashtag_list": hashtag_list}
        updated_post = update_post(db, post_id, post_data)
        return BaseResponse.on_success(PostSummaryDto(**updated_post.dict()))

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)


@router_post.delete("/posts/{post_id}", tags=["Post"], summary="게시글 삭제", description="게시글을 삭제합니다.",
                    response_model=BaseResponse[None])
async def delete_delete_post(
        post_id: UUID,
        token: str = Header(..., description="JWT token for authorization"),
):
    try:
        db: Session = SessionLocal()

        writer_id = extract_blog_id(token)

        # 삭제하고자 하는 게시글 조회
        post = get_post(db, post_id)
        if post is None or post.status == False:
            raise HTTPException(status_code=404, detail="Post not found or already deleted.")
        print("삭제 요청 온 게시글 정보: ", post)

        # 게시글 작성자인지 확인
        writer = get_blog(db, writer_id)  # 게시글을 삭제하고자 하는 사용자
        post_writer = get_blog(db, post.writer_id)
        if post_writer.id != writer.id:
            raise HTTPException(status_code=403, detail="Permission denied.")

        # 게시글 좋아요 정보 삭제
        user_post_likes = db.query(UserPostLike).filter(UserPostLike.post_id == post.id).all()
        for user_post_like in user_post_likes:
            delete_user_post_like(db, user_post_like.id)

        # 게시글 삭제
        delete_post(db, post_id)

        print("게시글이 삭제되었습니다.")

        return BaseResponse.on_success(None)

    except HTTPException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")
