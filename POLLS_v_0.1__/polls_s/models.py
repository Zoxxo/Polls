import datetime
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name="Вопрос")
    date_published = models.DateTimeField(verbose_name="Дата публикации", default=datetime.datetime.now())
    is_active = models.BooleanField(verbose_name="Опубликован")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question_id = models.ForeignKey(Question)
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(verbose_name="Голосов", default=0)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'