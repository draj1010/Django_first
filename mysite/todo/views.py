from django.shortcuts import render, redirect
from .models import todo, Userx
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import UserxSerializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	todos = todo.objects.all()
	userx = Userx.objects.all()
	if request.method == "POST":
		if 'todo_sub' in request.POST:
			task_title = request.POST['task_title']
			task = request.POST['task']
			author = request.POST['author']
			Todo = todo(task_title = task_title, task = task, author = Userx.objects.get(name = author))
			Todo.save()
			return redirect("todo_show") 
		if 'todo_del' in request.POST:
			task_id = request.POST['del_id']
			Todo = todo.objects.get(id = task_id)
			Todo.delete()

			return redirect("todo_show")

	return render(request,'todo_show.html',{'todos' : todos, 'userx' : userx})

@csrf_exempt
def userx_list(request):

	if request.method == 'GET':
		userx = Userx.objects.all()
		serializer = UserxSerializers(userx, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = UserxSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def userx_detail(request, pk):

	try:
		userx = Userx.objects.get(pk = pk)
	except Userx.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = UserxSerializers(userx)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = UserxSerializers(userx, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		userx.delete()
		return HttpResponse(status=204)

