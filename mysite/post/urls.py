from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('like/', views.like, name='like'),
        path('postadd/', views.postAdd, name='postadd'),
        path('modelpostadd/', views.modelpostform, name='modelpostadd'),
         ]