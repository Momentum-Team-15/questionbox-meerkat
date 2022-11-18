from django.shortcuts import render
from api.models import Question, Answer
from api.serializers import QuestionSerializer, AnswerSerializer
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from rest_framework.permissions import AllowAny

# Create your views here.
# For endpoints

class QuestionViewSet(ModelViewSet):
    queryset          = Question.objects.all()
    serializer_class  = QuestionSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Question.objects.filter(title__icontains=self.request.query_params.get("search"))
        else:
            results = Question.objects.annotate(
                total_answers=Count('answers')
            )
        return results

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)      

    def perform_destroy(self, instance):
        if self.request.user  == instance.user:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.user:
            serializer.save()


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]

