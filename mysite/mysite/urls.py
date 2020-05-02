"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('todo/', include('todo.urls')),
    path('redirect/', mysite),
    path('mysite/', index),
    path('', index),
    path('fun1', fun1),
    path('fun2', fun2),
    path('djangotutor/', tutorial.as_view()),
    path('setcookie',setcookie),
    path('getcookie',showcookie),
    path('deletecookie',deletecookie),
    path('createsession', createsession),
    path('getsession', getsession),
    path('deletesession', deletesession),
    path('subscribe/', include('subscribe.urls')),
    path('registration/', include('registration.urls')),
    path('upload/', include('profile_maker.urls')),
    path('home/',include('home.urls')),
    path('bootstr/',include('bootstr.urls')),
    path('ajax/', include('post.urls')),
    path('book/', include('book.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
