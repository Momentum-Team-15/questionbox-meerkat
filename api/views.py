from django.shortcuts import render
from api.models import Question, Answer
from api.serializers import QuestionSerializer, AnswerSerializer, FavoriteQuestionUpdateSerializer, AnswerAcceptSerializer
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, get_object_or_404, ListAPIView, UpdateAPIView, RetrieveUpdateAPIView
from django.db.models import Q
from rest_framework.response import Response
from .permissions import IsUserOrReadOnly



# Create your views here
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
            results = Question.objects.filter(Q(question__icontains=self.request.query_params.get("search"))| Q(title__icontains=self.request.query_params.get("search")))

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

# answer create view
# answer detail view 
# next week- user needs to be able to "accept" an answer - boolean field

# This is where the view starts for endpoint to create and list all answers 
class AnswerListCreateView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        #This is how you create a search code pulled form drf docs.
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            #Filtering answer objects for anything that has search term in title.
            results = Answer.objects.filter(answer__icontains=self.request.query_params.get("search"))
            return results



        # this is where we are only getting the answers related to the question
        return Answer.objects.filter(question_id=self.kwargs["question_pk"])
    # This is where we are changing the perform / create function within this API view 
    def perform_create(self, serializer):
        # This is where we are defining what a question is, also making sure the answer is saved to the right user and question
        # 
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        serializer.save(user=self.request.user, question=question)


#This view list the questions for one user.
class UserQuestions(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
# Below will change queryset to filter only a specific user questions.
    def get_queryset(self):
        return Question.objects.filter(user_id=self.kwargs["user_pk"])

#this view lists the questions that belong to the logged in user
class MyQuestions(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
# Below will change queryset to filter only the user logged in's questions.
    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)


class CreateUpdateFavoriteView(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = FavoriteQuestionUpdateSerializer
# filtering the question of a specific pk
    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(pk=self.kwargs["question_pk"])[0]
 # if it's not in favorites add it, otherwise delete it - toggle function   
    def update(self, request, *args, **kwargs):
        instance = self.get_queryset()
        if self.request.user not in instance.favorited_by.all():
            self.request.user.favorite_questions.add(instance)
        else:
            self.request.user.favorite_questions.remove(instance)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class FavoriteQuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.request.user.favorite_questions.all()

#This is the view for accepting an answer. -classy DRF RetrieveUpdateAPIView.
class AnswerAcceptedView(RetrieveUpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerAcceptSerializer
    #Below is where we are pulling in the permission i created in permissions.py 
    #now only the user who created the question can accept the answer.
    permission_classes = [IsUserOrReadOnly]


class MyAnswers(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)
