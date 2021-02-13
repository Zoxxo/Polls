from django.shortcuts import render
from rest_framework import generics
from polls_s.serializers import AnswerSerializer, QuestionSerializer
from polls_s.models import Question


class PollCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer, QuestionSerializer


class PollListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()





