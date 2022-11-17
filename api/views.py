from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Answer
from .serializers import AnswerSerializer

# Create your views here.
# For endpoints


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]
