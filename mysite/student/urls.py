from django.urls import path
from . import views

urlpatterns = [
	path('', views.student_show, name = 'student_show'),
	path('student/<int:st_id>/', views.student_show, name = 'student_show'),
	path('teacher', views.teacher_show, name = 'teacher_show'),
	path('product/<slug:p_slug>', views.product_display, name = 'product_display'),
]