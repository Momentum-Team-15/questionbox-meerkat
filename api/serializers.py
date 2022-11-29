from rest_framework import serializers 
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
     user = serializers.SlugRelatedField(read_only=True, slug_field="username")
     answers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
     total_answers  = serializers.IntegerField(read_only=True,)
     class Meta:
        model    = Question
        fields   = ['pk', 'title', 'created_date', 'question', 'user','answers', 'total_answers', 'favorites']

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Answer
        fields = ['pk', 'answer', 'user', 'created_date', 'question', 'favorites']
