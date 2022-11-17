from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.question}'

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=20)
    correct = models.BooleanField()
    def __str__(self):
        return f'{self.answer}-{self.question}'

class Cookie(models.Model):
    id = models.AutoField(primary_key=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f'cookie{self.id}'

class Maker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)

class Guest(models.Model):
    nickname = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.OneToOneField(Answer, on_delete=models.CASCADE, related_name='answer1')
    answer2 = models.OneToOneField(Answer, on_delete=models.CASCADE, related_name='answer2')
    answer3 = models.OneToOneField(Answer, on_delete=models.CASCADE, related_name='answer3')
    answer4 = models.OneToOneField(Answer, on_delete=models.CASCADE, related_name='answer4')
    answer5 = models.OneToOneField(Answer, on_delete=models.CASCADE, related_name='answer5')
    answers = []
    
    score = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['score', 'nickname']