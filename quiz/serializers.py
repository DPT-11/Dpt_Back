from rest_framework import serializers
from .models import *

class CookieChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ('user', 'cookie')

    def create(self, validated_data):
        data = Maker.objects.create(**validated_data)
        return data

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'

class CookieSerializer(serializers.ModelSerializer):
    # def get_cookie(self, obj):
    #     qs = Question.objects.filter(
    #         questionId__id=obj.id)
    class Meta:
        model = Cookie
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        data = Answer.objects.create(**validated_data)
        return data