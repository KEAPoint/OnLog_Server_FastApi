from fastapi import APIRouter, Query, Depends, HTTPException, Header, Body
from typing import Optional, List
from uuid import UUID
from schemas.auth import PostLoginRes, PostLogoutRes
from schemas.base import BaseResponse
from auth.jwt_handler import verify_access_token

router_auth = APIRouter()


@router_auth.get("/auth/kakao/login", tags=["Auth"], summary="카카오 계정을 통한 로그인", description="카카오 계정을 통해서 로그인을 진행합니다.",
                 response_model=BaseResponse[PostLoginRes])
async def kakao_login(code: str = Query(..., description="카카오 인가코드")):
    try:
        # 카카오 로그인
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


@router_auth.post("/auth/logout", tags=["Auth"], summary="블로그 로그아웃", description="블로그를 로그아웃 합니다.",
                  response_model=BaseResponse[PostLogoutRes])
async def user_logout(token: str = Header(..., description="사용자 refresh token")):
    try:
        # token 추출
        # 블로그 로그아웃
        response_data = {}

        return BaseResponse.on_create(response_data)

    except BaseException as e:
        return BaseResponse.from_exception(e)

    except Exception as e:
        return BaseResponse.from_exception(e)


def extract_token(token: str) -> str:
    parsed_token = token.split(" ")
    if parsed_token[0].lower() == "bearer":
        return parsed_token[1]
    return None
