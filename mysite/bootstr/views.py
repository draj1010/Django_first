from django.shortcuts import render
from .models import News
# Create your views here.
def home(request):
    news = News.objects.order_by('id').reverse()[:3]
    context = {'news':news}
    return render(request,'base.html',context)

def about(request):
    return render(request,'aboutus.html')

