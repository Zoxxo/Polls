from django.contrib import admin
from django.urls import path, include
from polls_s.views import *
app_name = 'poll'
urlpatterns = [
   path('poll/create/', PollCreateView()),
   path('all/', PollListView()),
   path('poll/detail/<int:pk>', PollDetailView())
]