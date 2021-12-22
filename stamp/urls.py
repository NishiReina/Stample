from django.urls import path
from . import views
from django.conf.urls.static import static # ← これ追加
from django.conf import settings 

urlpatterns = [
    path('', views.index, name='index'),
    path('original', views.original, name='original'),
    path('random_route', views.random_route, name='random_route'),
    path('original_route', views.original_route, name='original_route'),
    path('user_picturebook', views.user_picturebook, name='user_picturebook'),
    path('home', views.home, name='home'),
    path('route', views.route, name='route'),
    path('stamp', views.stamp, name='stamp'),
    path('detail/<uuid:shop_uuid>', views.detail, name='detail'),
    path('to_change_page', views.to_change_page, name='to_change_page'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)