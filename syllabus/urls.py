from django.contrib import admin
from django.urls import path
from syllabus import views

urlpatterns = [
    path('', views.indexView,name='index'),

]
