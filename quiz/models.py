from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.question}'

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=20)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20, null=True, blank=True)
    option3 = models.CharField(max_length=20, null=True, blank=True)
    option4 = models.CharField(max_length=20, null=True, blank=True)

class Cookie(models.Model):
    id = models.AutoField(primary_key=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f'cookie{self.id}'

class Maker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)