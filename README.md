# OnLog_Server_FastApi

### 프로젝트 개요
이 프로젝트는 Spring Boot를 기반으로 작업 된 [기존 프로젝트](https://github.com/KEAPoint/OnLog_Post_Server)를 참조하여 FastAPI로 구현하였습니다.

### 프로젝트 개발 환경
프로젝트는 Python 3.11.6 버전에서 개발되었습니다.

DB 설정에 관한 코드에서 Python 3.10 이상 버전에서만 작동하는 코드를 사용하였습니다.

자세한 내용은 [공식문서](https://fastapi.tiangolo.com/ko/tutorial/sql-databases/?h=sq)에서 확인 부탁드립니다.

### 프로젝트 개발/실행
1. 가상 환경 생성
```commandline
python3 -m venv venv
```

2. 가상 환경 활성화
```commandline
source venv/bin/activate
```

3. requirements 다운로드
```commandline
pip install -r requirements.txt
```

4. 프로그램 실행
```commandline
uvicorn main:app --port 8000 --reload
```

참고) 프로젝트가 실행 중인 환경에 한해 아래 URL에서 API 명세서를 확인할 수 있습니다
```commandline
http://localhost:8000/docs
http://localhost:8000/redoc
```
