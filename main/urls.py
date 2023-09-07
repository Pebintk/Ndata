from django.urls import path
from main.views import show_main

APP_NAME = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]