# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include

from .views import (
    ApicallApiView,
)

urlpatterns = [
    path('api', ApicallApiView.as_view()),
]