from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from typing import Optional, List
from uuid import UUID
from schemas.base import BaseResponse
from schemas.comment import CommentSummaryDto, PostCreateCommentReqDto, PutUpdateCommentReqDto
from auth.jwt_handler import extract_blog_id

router_comment = APIRouter()


@router_comment.post("/post/{post_id}/comments", tags=["Comment"], summary="댓글 작성", description="게시글에 댓글을 작성합니다.",
                     response_model=BaseResponse[CommentSummaryDto])
async def create_comment(
        token: str = Header(..., description="JWT token for authorization"),
        dto: PostCreateCommentReqDto = Body(...)
):
    try:
        # token 추출
        # 댓글 작성
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_comment.put("/post/{post_id}/comments/{comment_id}", tags=["Comment"], summary="댓글 수정",
                    description="사용자가 작성한 댓글의 내용을 수정합니다.",
                    response_model=BaseResponse[CommentSummaryDto])
async def update_comment(
        token: str = Header(..., description="JWT token for authorization"),
        dto: PutUpdateCommentReqDto = Body(...)
):
    try:
        # token 추출
        # 댓글 수정
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_comment.delete("/post/{post_id}/comments/{comment_id}", tags=["Comment"], summary="댓글 삭제",
                       description="사용자가 작성한 댓글을 삭제합니다.",
                       response_model=BaseResponse[None])
async def delete_comment(
        token: str = Header(..., description="JWT token for authorization"),
):
    try:
        # token 추출
        # 댓글 삭제
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)
