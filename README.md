# Dpt_Back

### 라이브러리 설치
    pip install django
    pip install pillow
    pip install djangorestframework

### API
### 퀴즈
### 등록 http://127.0.0.1:8000/quiz/cookie/ - POST
    {
        "user":"user(사용자 token 구현 후 넣어주세요)",
        "cookie":"쿠키"
    }
### 목록 http://127.0.0.1:8000/quiz/cookie/ - GET
    {
        "user":"현재는 user id / user(사용자 token 구현 후 넣어주세요)!",
        "cookie":"쿠키"
    }
### 쿠키 해당 질문 http://127.0.0.1:8000/quiz/cookie/<str:id> - GET
    {
        "id":쿠키 id,
        "questions":[
            질문1,
            질문2,
            질문3,
            질문4,
            질문5
        ]
    }
### 질문에 답변 옵션 추가하기 http://127.0.0.1:8000/quiz/make/answer/<str:user> - POST
    {
        "answer":"답변",
        "correct"true or false(정답인경우 true),
        "user":"현재는 user id",
        "question":"답변 해당 질문"
    }
### 질문 답변 옵션 수정 삭제하기 http://127.0.0.1:8000/quiz/make/answer/<str:id>/<str:user> - PUT, DELETE
    {
        "answer":"답변",
        "correct"true or false(정답인경우 true),
        "user":"현재는 user id",
        "question":"답변 해당 질문"
    }
### 질문 옵션 보기 http://127.0.0.1:8000/quiz/make/answer/<str:user> - GET(수정, 삭제 동일)
    {
        {
            "answer":"답변",
            "correct"true or false(정답인경우 true),
            "user":"현재는 user id",
            "question":"답변 해당 질문"
        }
        {
            "answer":"답변",
            "correct"true or false(정답인경우 true),
            "user":"현재는 user id",
            "question":"답변 해당 질문"
        }
        ...
    }