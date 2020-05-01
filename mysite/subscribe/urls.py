from django.urls import path
from . import views
urlpatterns = [
    path('', views.subscribe, name = 'subscribe'),
    path('demo/', views.demo, name = 'mass_mai'),
    path('email/', views.email, name='email'),
]