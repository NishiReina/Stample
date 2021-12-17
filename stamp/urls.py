from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('original', views.original, name='original'),
    path('random_route', views.random_route, name='random_route'),
    path('original_route', views.original_route, name='original_route'),
]