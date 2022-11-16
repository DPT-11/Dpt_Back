from django.urls import path
from .views import *

app_name = 'quiz'

urlpatterns = [
    path('cookie/', CookieChoice.as_view()),
    path('cookie/<str:id>', QuestionList.as_view()), 
    path('make/', AnswerCreate.as_view()), 
    path('question/', AnswerList.as_view()), 
]