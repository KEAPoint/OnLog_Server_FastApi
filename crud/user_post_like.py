from sqlalchemy.orm import Session
from models import UserPostLike
from schemas.post_like import PostLikeDto


def toggle_like(db: Session, blog_id: int, post_id: int) -> PostLikeDto:
    # 사용자가 게시물에 좋아요를 했는지 확인
    existing_like = (db.query(UserPostLike)
                     .filter(UserPostLike.user_id == blog_id, UserPostLike.post_id == post_id).first())

    if existing_like:
        # 이미 좋아요를 한 경우, 좋아요 취소
        db.delete(existing_like)
        db.commit()
        return PostLikeDto(blog_id=blog_id, post_id=post_id, is_liked=False)

    else:
        # 좋아요를 하지 않은 경우, 좋아요 생성
        new_like = UserPostLike(user_id=blog_id, post_id=post_id)
        db.add(new_like)
        db.commit()
        return PostLikeDto(user_id=blog_id, post_id=post_id, is_liked=True)
