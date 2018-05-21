from django.urls import path

from . import views

urlpatterns = [
    path('other', views.otherPage, name='otherPage'),
    path('', views.index, name='index'),
]