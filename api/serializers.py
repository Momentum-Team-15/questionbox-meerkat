from rest_framework import serializers 
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
     user = serializers.SlugRelatedField(read_only=True, slug_field="username")
     answers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
     total_answers  = serializers.IntegerField(read_only=True,)
     favorited_by = serializers.SlugRelatedField(read_only=True, many=True, slug_field="username")
     class Meta:
        model    = Question
        fields   = ['pk', 'title', 'created_date', 'question', 'user','answers', 'total_answers', 'favorited_by', 'favorite_count']

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Answer
        fields = ['pk', 'answer', 'user', 'created_date', 'question', 'accepted']

class FavoriteQuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title']

class AnswerAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['accepted']
        read_only = ['pk', 'answer', 'user', 'created_date', 'question']