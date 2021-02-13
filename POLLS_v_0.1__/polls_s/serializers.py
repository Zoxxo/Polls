from abc import ABC
from rest_framework import serializers
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Question
        fields = '__all__'
