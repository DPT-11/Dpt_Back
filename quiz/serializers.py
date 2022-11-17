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
    #     options = []    
    #     options.append(data.answer)
    #     options.append(data.option1)
    #     if data.option2 != '':
    #         options.append(data.option2)
    #     if data.option3 != '':
    #         options.append(data.option3)
    #     if data.option4 != '':
    #         options.append(data.option4)
    # # list로 답안 저장, options[1] 이 정답

    #     answer_dict = {}
    #     answer_dict[data.question] = options
    #     return answer_dict
class GuestSerializer(serializers.ModelSerializer):
    answers = []
    class Meta:
        model = Guest
        fields = ('nickname','user','answer1','answer2','answer3','answer4','answer5')

    def get_answers(self):
        lst = self.answers
        lst.append(self.answer1)
        lst.append(self.answer2)
        lst.append(self.answer3)
        lst.append(self.answer4)
        lst.append(self.answer5)
        return lst

    def create(self, validated_data):
        data = Guest.objects.create(**validated_data)
        return data