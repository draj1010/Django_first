from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'homepage'),
    path('others/', other, name = 'otherpage'),
    path('about/', about, name = 'about'),
]