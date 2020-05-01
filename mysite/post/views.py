from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import Postform
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', { 'posts': posts })
def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id = post_id )
        m = Like( post=likedpost )
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")



def postAdd(request):
    if request.method == 'POST':
        post_heading = request.POST['post_heading']
        post_text = request.POST['post_text']
        post_author = request.POST['post_author']

        Post.objects.create(
            post_heading = post_heading,
            post_text = post_text,
            post_author = post_author,
        )
        data = {
            'msg': post_heading + ' is added to posts',
        }
        return JsonResponse(data)
        
    context = {}
    return render(request, 'post/post_form.html',context)

def modelpostform(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        head = request.POST['post_heading']
        text = request.POST['post_text']
        val_flag = 1
        if len(head) < 5:
            err = "Heading must be more then 5 letters"
            val_flag = 0

        if form.is_valid() and val_flag == 1:
            form.save()
            data = {
                'success' : 1,
                'msg' : 'Submmited'
                
            }
            return JsonResponse(data)
        else:
            data = {
                'success' : 0,
                'err' : err
            }
            return JsonResponse(data)
    form = Postform()
    return render(request,'post/model_post_form.html',{'form':form})