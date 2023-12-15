from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from fastapi import status

####################  Base  ####################
DataT = TypeVar('DataT')


class BaseResponse(BaseModel, Generic[DataT]):
    is_success: bool
    code: int
    message: str
    data: Optional[DataT]

    @classmethod
    def on_success(cls, result: DataT):
        return cls(is_success=True, code=status.HTTP_200_OK, message="요청이 성공적으로 처리되었습니다.", data=result)

    @classmethod
    def on_create(cls, result: DataT):
        return cls(is_success=True, code=status.HTTP_201_CREATED, message="요청이 성공적으로 처리되어 새로운 리소스가 생성되었습니다.",
                   data=result)

    @classmethod
    def from_exception(cls, exception: BaseException):
        return cls(is_success=False, code=exception.error_code.status, message=exception.error_code.message)


####################  Auth  ####################
class TokensDto(BaseModel):
    grant_type: str = Field(..., title="token 타입")
    access_token: str = Field(..., title="access token")
    refresh_token: str = Field(..., title="refresh token")


class PostLoginRes(BaseModel):
    member_idx: UUID = Field(..., title="사용자 식별자")
    email: str = Field(..., title="사용자 이메일")
    profile_img_url: str = Field(..., title="사용자 프로필 이미지")
    token_info: TokensDto = Field(..., title="회원가입 성공 여부")


class PostLogoutRes(BaseModel):
    is_success: bool = Field(..., title="회원가입 성공 여부")


class SocialAccountUserInfo(BaseModel):
    user_name: str = Field(..., title="사용자 이름")
    user_email: str = Field(..., title="사용자 이메일")
    profile_img_url: str = Field(..., title="사용자 프로필 이미지")


####################  Blog  ####################
class BlogDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    blog_name: str = Field(..., title="블로그 이름")
    blog_nickname: str = Field(..., title="블로그 별명")
    blog_profile_img: str = Field(..., title="블로그 프로필")
    blog_intro: str = Field(..., title="블로그 한 줄 소개")
    blog_theme_img: str = Field(..., title="블로그 테마 이미지")


class BlogProfileDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    blog_name: str = Field(..., title="블로그 이름")
    blog_nickname: str = Field(..., title="블로그 별명")
    blog_profile_img: str = Field(..., title="블로그 프로필")
    blog_intro: str = Field(..., title="블로그 한 줄 소개")
    blog_theme_img: str = Field(..., title="블로그 테마 이미지")
    post_count: int = Field(..., title="작성한 글 개수")
    like_count: int = Field(..., title="좋아요 받은 개수")
    subscriber_count: int = Field(..., title="구독자 수")


class PostCreateBlogReqDto(BaseModel):
    blog_name: str = Field(..., title="블로그 이름")
    blog_nickname: str = Field(..., title="블로그 별명")
    blog_profile_img: str = Field(..., title="블로그 프로필")
    blog_intro: str = Field(..., title="블로그 한 줄 소개")


class PutUpdateBlogReqDto(BaseModel):
    blog_name: str = Field(..., title="블로그 이름")
    blog_nickname: str = Field(..., title="블로그 별명")
    blog_profile_img: str = Field(..., title="블로그 프로필")
    blog_intro: str = Field(..., title="블로그 한 줄 소개")


####################  Blog - Follow  ####################
class BlogFollowDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    follow_id: UUID = Field(..., title="팔로우 블로그 식별자")
    is_following: bool = Field(..., title="해당 블로그를 팔로잉 하고 있는지 여부")


####################  Category  ####################
class CategoryDto(BaseModel):
    id: int = Field(..., title="카테고리 식별자")
    name: str = Field(..., title="카테고리 이름")
    order: int = Field(..., title="카테고리 순서")


class PostCreateCategoryReqDto(BaseModel):
    name: str = Field(..., title="생성할 카테고리 이름")


class PutCategoryUpdateReqDto(BaseModel):
    name: str = Field(..., title="수정할 카테고리 이름")


####################  Comment  ####################
class CommentDto(BaseModel):
    comment_id: UUID = Field(..., title="댓글 식별자")
    content: str = Field(..., title="댓글 내용")
    modified: bool = Field(..., title="댓글 수정 여부")
    ref: int = Field(..., title="그룹")
    ref_order: int = Field(..., title="그룹 순서")
    step: int = Field(..., title="댓글의 계층")
    parent_comment_id: UUID = Field(..., title="부모 댓글의 ID")
    answer_num: int = Field(..., title="해당 댓글의 자식 댓글의 수")
    created_at: datetime = Field(..., title="댓글 작성 시간")
    post_id: UUID = Field(..., title="댓글이 달린 게시글 식별자")
    writer: BlogDto = Field(..., title="댓글 작성자의 블로그 식별자")
    comment_liked: bool = Field(..., title="댓글 좋아요 하고 있는지 여부")
    likes_count: int = Field(..., title="댓글 좋아요 갯수")


class CommentSummaryDto(BaseModel):
    comment_id: UUID = Field(..., title="댓글 식별자")
    content: str = Field(..., title="댓글 내용")
    modified: bool = Field(..., title="댓글 수정 여부")
    ref: int = Field(..., title="그룹")
    ref_order: int = Field(..., title="그룹 순서")
    step: int = Field(..., title="댓글의 계층")
    parent_comment_id: UUID = Field(..., title="부모 댓글의 ID")
    answer_num: int = Field(..., title="해당 댓글의 자식 댓글의 수")
    created_at: datetime = Field(..., title="댓글 작성 시간")


class PostCreateCommentReqDto(BaseModel):
    content: str = Field(..., title="댓글 내용")
    parent_comment_id: Optional[UUID] = Field(None, title="부모댓글의 ID (null 가능)")


class PutUpdateCommentReqDto(BaseModel):
    content: str = Field(..., title="댓글 내용")


####################  Comment - Like  ####################
class CommentLikeDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    comment_id: UUID = Field(..., title="댓글 식별자")
    is_liked: bool = Field(..., title="사용자가 해당 댓글에 대해 '좋아요' 상태인지 나타내는 플래그")


####################  Hashtag  ####################
class HashtagDto(BaseModel):
    id: int = Field(..., title="해시태그 식별자")
    name: str = Field(..., title="해시태그 내용")


####################  Topic  ####################
class TopicDto(BaseModel):
    id: int = Field(..., title="주제 식별자")
    name: str = Field(..., title="주제 이름")


####################  Post  ####################


class PostDto(BaseModel):
    post_id: UUID = Field(..., title="게시글 식별자")
    post_hits: int = Field(..., title="게시글 방문 횟수")
    title: str = Field(..., title="게시글 제목")
    content: str = Field(..., title="게시글 내용")
    summary: str = Field(..., title="게시글 3줄 요약")
    thumbnail_link: str = Field(..., title="게시글 thumbnail 사진 위치")
    post_liked: bool = Field(..., title="게시글을 좋아요 하고 있는지 여부")
    likes_count: int = Field(..., title="게시글 좋아요 갯수")
    is_public: bool = Field(..., title="게시글 공개 여부")
    is_modified: bool = Field(..., title="게시글 수정 여부")
    topic: TopicDto = Field(..., title="게시글 주제")
    category: CategoryDto = Field(..., title="게시글 카테고리")
    hashtag_list: List[HashtagDto] = Field(..., title="해시태그 리스트")
    comments_counts: int = Field(..., title="게시글 댓글 갯수")
    comments: List[CommentDto] = Field(..., title="게시글 댓글")
    writer: BlogDto = Field(..., title="작성자")
    created_at: datetime = Field(..., title="게시글 생성 시점")


class PostSummaryDto(BaseModel):
    post_id: UUID = Field(..., title="게시글 식별자")
    title: str = Field(..., title="게시글 제목")
    content: str = Field(..., title="게시글 내용")
    summary: str = Field(..., title="게시글 3줄 요약")
    thumbnail_link: str = Field(..., title="게시글 thumbnail 사진 위치")
    likes_count: int = Field(..., title="게시글 좋아요 갯수")
    category: CategoryDto = Field(..., title="게시글 카테고리")
    topic: TopicDto = Field(..., title="게시글 주제")
    comments_counts: int = Field(..., title="게시글 댓글 갯수")
    writer: BlogDto = Field(..., title="작성자")
    created_at: datetime = Field(..., title="게시글 작성 시간")


class PostWithRelatedPostsDto(BaseModel):
    data: PostDto = Field(..., title="사용자가 조회한 게시글")
    related_posts: List[PostSummaryDto] = Field(..., title="같은 카테고리의 다른 게시글들")


class PostWritePostReqDto(BaseModel):
    title: str = Field(..., title="게시글 제목")
    content: str = Field(..., title="게시글 내용")
    summary: str = Field(..., title="게시글 3줄 요약")
    thumbnail_link: str = Field(..., title="게시글 thumbnail 사진 위치")
    is_public: bool = Field(..., title="게시글 공개 여부")
    category_id: int = Field(..., title="게시글 카테고리")
    hashtag_list: List[str] = Field(..., title="게시글 hashtag")
    topic_id: int = Field(..., title="게시글 주제 식별자")


class PutModifyPostReqDto(BaseModel):
    title: str = Field(..., title="게시글 제목")
    content: str = Field(..., title="게시글 내용")
    summary: str = Field(..., title="게시글 3줄 요약")
    thumbnail_link: str = Field(..., title="게시글 thumbnail 사진 위치")
    is_public: bool = Field(..., title="게시글 공개 여부")
    category_id: int = Field(..., title="게시글 카테고리")
    hashtag_list: List[str] = Field(..., title="게시글 hashtag")
    topic_id: int = Field(..., title="게시글 주제 식별자")


####################  Post - Like  ####################
class PostLikeDto(BaseModel):
    blog_id: UUID = Field(..., title="블로그 식별자")
    post_id: UUID = Field(..., title="게시글 식별자")
    is_liked: bool = Field(..., title="사용자가 해당 게시글에 대해 '좋아요' 상태인지 나타내는 플래그")
