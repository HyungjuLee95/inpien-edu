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

## 다음 단계 제안 (Phase 2)

- 임박/만료 알림 로직
- 우선 소비 목록 API
- 만료 임계일 설정 기능
