from django.shortcuts import render
from api.models import Question, Answer
from api.serializers import QuestionSerializer, AnswerSerializer
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from rest_framework.permissions import AllowAny

# Create your views here.
# For endpoints

class QuestionViewSet(ModelViewSet):
    #This is question models view set.
    queryset          = Question.objects.all()
    serializer_class  = QuestionSerializer

    def get_queryset(self):
        #This is how you create a search code pulled form drf docs.
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            #Filtering question objects for anything that has search term in title.
            results = Question.objects.filter(title__icontains=self.request.query_params.get("search"))
        else:
            results = Question.objects.annotate(
                #This allows total number of answers for each question in json.
                total_answers=Count('answers')
            )
        return results

    def perform_create(self, serializer):
        #This means that question will be saved to users account.
        serializer.save(user=self.request.user)      

    def perform_destroy(self, instance):
        #This means that only the user can delete there own question.
        if self.request.user  == instance.user:
            instance.delete()

    def perform_update(self,serializer):
        #This means that the update will only save if the user is the creator of the question.
        if self.request.user == serializer.instance.user:
            serializer.save()


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]

