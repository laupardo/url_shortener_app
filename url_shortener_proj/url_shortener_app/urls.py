from django.shortcuts import render
from django.urls import path
from .views import index, redirect_to_original_url

urlpatterns = [
    #gets data an generates short url
    path('', index, name='index'),
    #redirects
    path('<str:identifier>/', redirect_to_original_url, name='redirect_to_original_url'),
]
