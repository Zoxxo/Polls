from django.shortcuts import render
from rest_framework import generics
from polls_s.serializers import AnswerSerializer, ChoiceSerializer, QuestionSerializer, PollSerializer
from polls_s.models import Poll


class PollCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer, ChoiceSerializer, QuestionSerializer, PollSerializer


class PollListView(generics.ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()





