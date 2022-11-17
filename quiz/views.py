from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.views import View
from django.http import Http404, HttpResponse
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
import json

# Create your views here.

# 사용자에게 쿠키 값 넘기기
class CookieChoice(generics.ListCreateAPIView):
    serializer_class = CookieChoiceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Maker.objects.all()

# 쿠키마다 질문 보이기 -> question 값 id-> string 후에 수정
class QuestionList(generics.RetrieveAPIView):
    serializer_class = CookieSerializer
    queryset = Cookie.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_question(self, request):
        questions = []
        question = Question.objects.all()
        for q in question:
            if q in self.queryset:
                q_data = {
                    'question':q.question,
                }
                questions.append(q_data)
        return questions

# 답 등록 및 전체 question 보기
class AnswerCreate(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all()

        # 사용자 등록 답안만 가져온다
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

# 답 수정, 삭제 가능
class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all()
    lookup_field = 'id'

        # 사용자 등록 답안만 가져온다
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

# 등록한 답 보기
class AnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all()

    # 사용자 등록 답안만 가져온다
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    # -> options = [] 넣을 예정

class GuestCreate(generics.ListCreateAPIView):
    serializer_class = GuestSerializer
    permission_classes = []
    queryset = Guest.objects.all()

    # 사용자 등록 답안만 가져온다
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    # def get_answers(self):
    #     self.answers = []
    #     lst = self.answers
    #     lst.append(self.answer1)
    #     lst.append(self.answer2)
    #     lst.append(self.answer3)
    #     lst.append(self.answer4)
    #     lst.append(self.answer5)
    #     return lst

def score(request, pk):
    user = get_object_or_404(User, pk=pk)
    guest = get_object_or_404(Guest, pk)
    answer = Answer.objects.filter(user==request.user)
    guest.score = 0

    if request.POST['answer1'] :
        answer = Answer.objects.filter(answer.question == guest.answer1.question)
        if answer.correct == True:
            guest.score += 1
    if request.POST['answer2'] :
        answer = Answer.objects.filter(answer.question == guest.answer2.question)
        if answer.correct == True:
            guest.score += 1
    if request.POST['answer3'] :
        answer = Answer.objects.filter(answer.question == guest.answer3.question)
        if answer.correct == True:
            guest.score += 1
    if request.POST['answer4'] :
        answer = Answer.objects.filter(answer.question == guest.answer4.question)
        if answer.correct == True:
            guest.score += 1
    if request.POST['answer5'] :
        answer = Answer.objects.filter(answer.question == guest.answer5.question)
        if answer.correct == True:
            guest.score += 1
    guest.save()