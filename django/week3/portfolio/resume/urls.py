from django.urls import path
from django.contrib import admin

from . import views

app_name='resume'
urlpatterns = [
    path('resume/', views.home, name='home'),
]
