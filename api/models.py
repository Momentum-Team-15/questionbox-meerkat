from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField
# Create your models here.


class User(AbstractUser):
    pet_amount = models.PositiveIntegerField(blank=True, null=True)
    pet_types = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username}"


class Question(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f"{self.title}"


class Answer(models.Model):
    answer = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"{self.answer}"