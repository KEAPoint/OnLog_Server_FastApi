from sqlalchemy.orm import Session
from models import Comment, UserCommentLike
from schemas.comment_like import CommentLikeDto


def toggle_like(db: Session, blog_id: str, comment_id: str) -> CommentLikeDto:
    # 댓글 좋아요 정보 조회
    user_comment_like = (db.query(UserCommentLike)
                         .filter(UserCommentLike.blog.blog_id == blog_id,
                                 UserCommentLike.comment.comment_id == comment_id).first())

    if user_comment_like:
        # 댓글 좋아요 했던 상태면 좋아요 취소
        db.delete(user_comment_like)
        decrease_comment_likes_count(db, comment_id)  # 좋아요 취소 시 개수 감소
        is_liked = False

    else:
        # 댓글 좋아요 하지 않았던 상태면 좋아요 추가
        new_like = UserCommentLike(blog_id=blog_id, comment_id=comment_id)
        db.add(new_like)
        increase_comment_likes_count(db, comment_id)  # 좋아요 추가 시 개수 증가
        is_liked = True

    db.commit()

    # 결과 리턴
    return CommentLikeDto(blog_id=blog_id, comment_id=comment_id, is_liked=is_liked)


def increase_comment_likes_count(db: Session, comment_id: str):
    try:
        # 댓글 정보 조회
        comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()

        if comment:
            # 댓글 좋아요 개수 증가
            comment.likes_count += 1

            # DB에 반영
            db.commit()

    except Exception as e:
        # 예외 처리 로직 추가
        raise e


def decrease_comment_likes_count(db: Session, comment_id: str):
    try:
        # 댓글 정보 조회
        comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()

        if comment:
            # 댓글 좋아요 개수 줄이기
            if comment.likes_count > 0:
                comment.likes_count -= 1

            # DB에 반영
            db.commit()

    except Exception as e:
        # 예외 처리 로직 추가
        raise e
