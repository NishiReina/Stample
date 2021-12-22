from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('first_original', views.signup_original, name='signup_original'),
    path('first_random', views.signup_random, name='signup_random'),
    path('change', views.change, name='change'),
]