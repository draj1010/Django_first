from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'todo_show'),
	path('userx/', views.userx_list, name = 'user_rest_list'),
	path('userx/<int:pk>', views.userx_detail, name = 'user_rest_detail'),

]