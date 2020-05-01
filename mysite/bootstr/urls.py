from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name = 'base_page'),
    path('about', about,name = 'about_page'),
]