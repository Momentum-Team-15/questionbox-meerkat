from .models import Answer
from rest_framework import serializers


class AnswerSerializer(serializers.AnswerSerializer):
    class Meta:
        model = Answer
        fields = ['__all__']
