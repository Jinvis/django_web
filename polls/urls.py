from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video/<name>/', views.video, name='video'),
]