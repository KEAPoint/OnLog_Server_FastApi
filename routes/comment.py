from fastapi import APIRouter, HTTPException, Header, Body, FastAPI
from uuid import UUID
from database import SessionLocal
from schemas.base import BaseResponse
from sqlalchemy.orm import Session
from schemas.comment import CommentSummaryDto, PostCreateCommentReqDto, PutUpdateCommentReqDto
from auth.jwt_handler import extract_blog_id
from crud.comment import create_comment, update_comment, delete_comment
from models import Post, Comment
from loguru import logger

router_comment = APIRouter()


@router_comment.post("/post/{post_id}/comments", tags=["Comment"], summary="댓글 작성", description="게시글에 댓글을 작성합니다.",
                     response_model=BaseResponse[CommentSummaryDto])
async def post_create_comment(
        post_id: UUID,
        token: str = Header(..., description="JWT token for authorization"),
        dto: PostCreateCommentReqDto = Body(...)
):
    try:
        db: Session = SessionLocal()

        # 게시글 조회
        post = db.query(Post).filter(Post.id == post_id).first()
        if post is None or not post.status:
            raise HTTPException(status_code=404, detail="Post not found")

        ref = ref_order = step = answer_num = 1
        parent_num = dto.parent_comment_id

        # if parent_num is not None:  # 부모 댓글이 있는 경우 (대댓글)
        #     parent_comment = db.query(Comment).filter(Comment.id == parent_num).first()
        #     if parent_comment is None:
        #         raise HTTPException(status_code=404, detail="Parent Comment not found")
        #
        #     ref = parent_comment.ref
        #     step = parent_comment.step + 1
        #     ref_order = update_and_get_current_ref_order(parent_comment)
        #
        #     parent_comment.update_number_of_child_comment()

        # 부모 댓글이 없는 경우 (댓글)
        ref = db.query(Comment).filter(Comment.post == post).order_by(
            Comment.ref.desc()).first().ref + 1

        # 댓글 생성
        comment_data = {
            "content": dto.content,
            "modified": False,
            "ref": ref,
            "ref_order": ref_order,
            "step": step,
            "parent_num": parent_num,
            "answer_num": answer_num,
            "likes_count": 0,
            "post": post,
            "writer": post.writer,  # 게시글 작성자가 댓글 작성자가 된다고 가정
        }
        comment = create_comment(db, comment_data)

        post.write_comment()
        logger.info(f"사용자 ({post.writer.id})가 게시글 ({post.id})에 댓글({comment.id})을 작성하는 데 성공하였습니다.")
        return BaseResponse.on_create(CommentSummaryDto(**comment.dict()))

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")


@router_comment.put("/post/{post_id}/comments/{comment_id}", tags=["Comment"], summary="댓글 수정",
                    description="사용자가 작성한 댓글의 내용을 수정합니다.",
                    response_model=BaseResponse[CommentSummaryDto])
async def put_update_comment(
        comment_id: UUID,
        token: str = Header(..., description="JWT token for authorization"),
        dto: PutUpdateCommentReqDto = Body(...)
):
    try:
        db: Session = SessionLocal()

        blog_id = UUID(extract_blog_id(token))

        comment_data = dto.dict()
        comment_data["blog_id"] = blog_id
        comment = update_comment(db, comment_id, comment_data)
        return BaseResponse.on_create(comment)

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")


@router_comment.delete("/post/{post_id}/comments/{comment_id}", tags=["Comment"], summary="댓글 삭제",
                       description="사용자가 작성한 댓글을 삭제합니다.",
                       response_model=BaseResponse[None])
async def delete_delete_comment(
        comment_id: UUID,
        token: str = Header(..., description="JWT token for authorization"),
):
    try:
        db: Session = SessionLocal()

        blog_id = UUID(extract_blog_id(token))

        # 댓글 삭제
        delete_comment(db, comment_id)
        return {"message": "Comment has been deleted successfully"}

    except BaseException as e:
        print(e.detail)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error.")