from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/original', views.original, name='original'),
    path('/random', views.random, name='random'),
]