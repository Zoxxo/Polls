from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'is_active']}
         ),
        ('Информация о дате',
         {'fields': ['date_published'],
          'classes': ['collapse']}
         ),
    ]
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
