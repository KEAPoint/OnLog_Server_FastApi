from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from typing import Optional, List
from uuid import UUID
from schemas import BaseResponse, PostSummaryDto, PostWithRelatedPostsDto, PostWritePostReqDto, PutModifyPostReqDto
from auth.jwt_handler import verify_access_token

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
        topicName: Optional[str] = Query(None),
        hashtag: Optional[str] = Query(None),
        blogId: Optional[UUID] = Query(None),
        categoryId: Optional[int] = Query(None),
        isPublic: Optional[bool] = Query(None),
        pageable: Pageable = Depends(Pageable),
):
    try:
        my_blog_id = verify_access_token(token)
        my_blog_id_uuid = UUID(my_blog_id)

        # Access pageable.page and pageable.size in your logic
        page_number = pageable.page
        items_per_page = pageable.size

        # Call the FastAPI equivalent of postService.getRecentPosts
        # Assign the result to response_data
        response_data = {}

        return BaseResponse.on_success(response_data)

    except HTTPException as e:
        return BaseResponse.from_exception()

    except Exception as e:
        return BaseResponse.from_exception()


@router_post.get("/posts/{post_id}", tags=["Post"], summary="특정 게시글 조회", description="게시글 ID에 따른 게시글 상세내용을 조회합니다.(1개)",
                 response_model=BaseResponse[PostWithRelatedPostsDto])
async def get_post(
        token: str = Header(..., description="JWT token for authorization"),
):
    # token 검증
    # 게시글 조회
    response_data = {}
    return BaseResponse.on_success(response_data)


@router_post.post("/posts", tags=["Post"], summary="게시글 작성", description="게시글을 작성합니다.",
                  response_model=BaseResponse[PostSummaryDto])
async def write_post(
        token: str = Header(..., description="JWT token for authorization"),
        dto: PostWritePostReqDto = Body(...),
):
    # token 검증
    # 게시글 작성
    response_data = {}
    return BaseResponse.on_create(response_data)


@router_post.put("/posts/{post_id}", tags=["Post"], summary="게시글 수정", description="게시글을 수정합니다.",
                 response_model=BaseResponse[PostSummaryDto])
async def update_post(
        token: str = Header(..., description="JWT token for authorization"),
        dto: PutModifyPostReqDto = Body(...),
):
    # token 검증
    # 게시글 수정
    response_data = {}
    return BaseResponse.on_create(response_data)


@router_post.delete("/posts/{post_id}", tags=["Post"], summary="게시글 삭제", description="게시글을 삭제합니다.",
                    response_model=BaseResponse[None])
async def delete_post(
        token: str = Header(..., description="JWT token for authorization"),
):
    # token 검증
    # 게시글 삭제
    return BaseResponse.on_success(None)
