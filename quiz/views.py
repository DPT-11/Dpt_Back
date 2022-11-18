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

# 답 등록 및 전체 QUESTION 보기
class NewAnswerCreate(generics.ListCreateAPIView):
    serializer_class = NewAnswerSerializer
    permission_classes = [IsAuthenticated]
    queryset = NewAnswer.objects.all()

        # 사용자 등록 답안만 가져온다
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

# 등록한 답 보기
class AnswerList(generics.ListAPIView):
    serializer_class = NewAnswerSerializer
    permission_classes = [IsAuthenticated]
    queryset = NewAnswer.objects.all()

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