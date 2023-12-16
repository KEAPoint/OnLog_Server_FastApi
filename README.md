# OnLog_Server_FastApi

## 🌐 프로젝트 개요
이 프로젝트는 Spring Boot를 기반으로 작업 된 [🔗기존 프로젝트](https://github.com/KEAPoint/OnLog_Post_Server)를 참조하여 FastAPI로 구현하였습니다.


## 🛠️ 프로젝트 개발 환경
프로젝트는 아래 환경에서 개발되었습니다.

> OS: macOS Sonoma, Ventura   
IDE: Pycharm  
Python: 3.11.6

DB 설정에 관한 코드에서 Python 3.10 이상 버전에서만 작동하는 코드를 사용하였습니다.

자세한 내용은 [공식문서](https://fastapi.tiangolo.com/ko/tutorial/sql-databases/?h=sq)에서 확인 부탁드립니다.

## 🔗 프로젝트 구조
```text
.
├── .dockerignore          🚫 Docker 이미지 생성 시 무시하는 파일 목록
├── .env                   🔐 프로젝트에서 사용하는 환경 변수 설정 파일
├── .gitignore             🙈 Git 버전 관리 시 무시하는 파일 목록
├── Dockerfile             🐳 Docker 이미지 생성을 위한 스크립트
├── README.md              📚 프로젝트에 대한 설명과 사용 방법 등을 담은 문서
├── __init__.py            💡 패키지 초기화 파일
├── __pycache__            🗂️ 파이썬이 컴파일한 버전의 파일을 저장하는 디렉토리
├── auth                   🔑 사용자 인증을 위한 코드를 담고 있는 디렉토리
├── crud                   💾 데이터의 생성, 조회, 수정, 삭제를 위한 코드를 담고 있는 디렉토리
├── database.py            🗄️ 데이터베이스 연결 및 세션 관리를 위한 파일
├── main.py                🚀 프로그램의 시작점
├── models.py              📃 데이터베이스 테이블 구조를 정의하는 파일
├── requirements.txt       📌 프로젝트에서 필요한 파이썬 패키지 목록
├── routes                 🚦 웹 요청을 처리하는 라우터를 정의하는 디렉토리
└── schemas                📝 데이터 검증 및 직렬화/역직렬화를 위한 스키마를 정의하는 디렉토리

```

## ✅ 프로젝트 개발/실행
해당 프로젝트를 추가로 개발 혹은 실행시켜보고 싶으신 경우 아래의 절차에 따라 진행해주세요

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

4. `.env` 파일 생성
```commandline
touch .env
```

5. Database 정보 및 Secret key 정보 입력
```text
SQLALCHEMY_DATABASE_URL = {DATABASE_INFORMATION}
SECRET_KEY = {SECRET_KEY}
```
참고) DATABASE_INFORMATION은 다음과 같이 작성해주시면 됩니다. `postgresql://user:password@postgresserver/db`

자세한 내용은 [공식문서](https://fastapi.tiangolo.com/ko/tutorial/sql-databases/?h=sql) 확인 부탁드립니다.

6. 프로그램 실행
```commandline
uvicorn main:app --port 8000 --reload
```

참고) 프로젝트가 실행 중인 환경에 한해 아래 URL에서 API 명세서를 확인할 수 있습니다
```commandline
http://localhost:8000/docs
http://localhost:8000/redoc
```

## 📝 프로젝트 회고
프로젝트를 개발하면서 다음과 같은 아쉬움이 있었습니다.

1. 프로젝트 퀄리티
2. 테스트 미진행

FastAPI의 경우는 백엔드를 개발하고 있는 팀원들의 주 언어가 아니다 보니 프로젝트의 구조가 FastAPI로 개발하는 개발자에 비해 퀄리티가 매우 아쉽습니다.

또한 기존 언어로 개발한 코드의 테스트와 클라우드의 제공이 늦어짐에 따라 후반부에 시스템을 구축하는데 시간을 많이 할애하여 코드를 검증하지 못한 점 또한 아쉬웠습니다.

## ❗️ 프로젝트 개선점
1. 코드 퀄리티
2. 서비스 검증

