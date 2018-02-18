from django.urls import path
from django.contrib import admin

from . import views

app_name='resume'
urlpatterns = [
    path('', views.home, name='home'),
]
