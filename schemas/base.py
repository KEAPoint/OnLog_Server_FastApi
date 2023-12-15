from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel, Field
from fastapi import status

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
