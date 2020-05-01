from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Teacher, Products 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def student_show(request, st_id):
	student = Student.objects.filter(id = st_id)

	return render(request, 'student/student_show.html', {'student' : student})

def teacher_show(request):
	# teacher_list = Teacher.objects.order_by('card_no')
	teacher_list = Teacher.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(teacher_list, 1)
	try:
		teacher = paginator.page(page)
	except PageNotAnInteger:
		teacher = paginator.page(1)
	except EmptyPage:
		teacher = paginator.page(paginator.num_pages)
	return render(request, 'teacher/teacher_show.html', {'teacher' : teacher})

def product_display(request, p_slug):
	product = Products.objects.filter(slug = p_slug)

	return render(request, 'products/product_display.html', {'product' : product})