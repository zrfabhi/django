
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index , name='index'),
    path('login', views.loginuser , name='login'),
    path('logout', views.logoutuser , name='logout'),
    path('upload', views.upload, name='upload'),
    
  
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)