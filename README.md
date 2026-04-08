# Inpien Edu - Home Inventory & Expiry Manager (Phase 1)

가정용 식품/생활용품의 재고와 유통기한을 관리하기 위한 MVP 프로젝트입니다.

## Phase 1 범위

- 사용자 회원가입/로그인(JWT)
- 품목(Item) 등록/조회
- 보관 위치(Location) 등록/조회
- 재고 배치(Inventory Batch) 등록/조회
- PostgreSQL DDL 제공

> 소비/폐기 처리, 임박 알림, 재구매 자동화는 다음 Phase에서 확장합니다.

## 프로젝트 구조

```bash
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── deps.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── security.py
│   │   └── routers/
│   │       ├── auth.py
│   │       ├── items.py
│   │       ├── locations.py
│   │       └── inventory.py
│   └── requirements.txt
└── db/
    └── schema.sql
```

## 원격 저장소 연동 & `git pull` 명령어

> 아래에서 `<REMOTE_URL>` 과 `<BRANCH>` 는 본인 저장소 정보로 바꿔서 사용하세요.

### A) 이미 프로젝트 폴더가 있고, 원격만 연결할 때

```bash
# 현재 폴더가 /workspace/inpien-edu 라는 가정
cd /workspace/inpien-edu

# 원격 확인
git remote -v

# 원격이 없다면 추가
git remote add origin <REMOTE_URL>

# 기본 브랜치 가져오기
git fetch origin

# 내 로컬 브랜치를 원격 브랜치와 연결
# 예: git branch --set-upstream-to=origin/main main
git branch --set-upstream-to=origin/<BRANCH> <BRANCH>

# 최신 변경 가져오기
git pull --rebase
```

### B) 원격 저장소를 처음부터 클론할 때

```bash
git clone <REMOTE_URL>
cd <REPO_DIR>
git checkout <BRANCH>
git pull --rebase
```

### C) pull 충돌 시 빠른 처리

```bash
# 충돌 파일 확인
git status

# 파일 수정 후
git add .
git rebase --continue

# rebase 취소
git rebase --abort
```

## 실행 방법 (Backend)

### 1) 의존성 설치

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) DB 생성/DDL 적용

```bash
createdb inpien_edu
psql -d inpien_edu -f ../db/schema.sql
```

### 3) 환경변수 설정

`DATABASE_URL` 환경변수를 설정합니다.

```bash
export DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/inpien_edu"
```

### 4) 서버 실행

```bash
uvicorn app.main:app --reload
```

- Swagger UI: `http://127.0.0.1:8000/docs`
- Health Check: `GET /health`

## 주요 API

- `POST /auth/signup`
- `POST /auth/login`
- `GET/POST /items`
- `GET/POST /locations`
- `GET/POST /inventory/batches`

## 최소 점검 명령어

```bash
# 문법 체크
python -m compileall backend/app
```

## 다음 단계 제안 (Phase 2)

- 임박/만료 알림 로직
- 우선 소비 목록 API
- 만료 임계일 설정 기능
