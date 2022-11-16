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
### 질문에 답변 만들기 http://127.0.0.1:8000/quiz/make/ - POST
    {
        "answer":"정답(필수 입력)",
        "option1":"오답(필수 입력)",
        "option2":"오답(필수 입력 아님)",
        "option3":"오답(필수 입력 아님)",
        "option4":"오답(필수 입력 아님)",
        "user":"현재는 user id / user(사용자 token 구현 후 넣어주세요)!",
        "question":"질문"
    }
### 질문 답변 전체 목록 http://127.0.0.1:8000/quiz/question/ - GET
    {
        "answer":"정답 입력 값",
        "option1":"오답 입력 값",
        "option2":"오답 입력 값 (입력 없을 경우 "")",
        "option3":"오답 입력 값 (입력 없을 경우 "")",
        "option4":"오답 입력 값 (입력 없을 경우 "")",
        "user":"현재는 user id / user(사용자 token 구현 후 넣어주세요)!",
        "question":"질문"
    }