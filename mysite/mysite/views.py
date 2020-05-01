from django.shortcuts import render, redirect 
from django.http import HttpResponse
import time
from django.views.generic.base import RedirectView 

def index(request):
    html = HttpResponse("<h1>index page</h1><script>console.log('what are you looking for in console?')</script>")
    html.set_cookie('key','value',max_age=None)
    return html

def mysite(request):
   	return redirect('/mysite')

def fun1(request):
	time.sleep(0.3)
	return redirect('/fun2')

def fun2(request):
	time.sleep(0.3)
	return redirect('/fun1')

class tutorial(RedirectView):
	url = "http://google.com"

def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('check')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')

def setcookie(request):
	html = HttpResponse('Welcome')
	if request.COOKIES.get('visits'):
		html.set_cookie('check','Welcome Back')
		value = int(request.COOKIES.get('visits'))
		html.set_cookie('visits', value + 1)
	else:
		value = 1
		text = "Welcome for the first time"
		html.set_cookie('visits',value)
		html.set_cookie('check',text)
	return html

def deletecookie(request):
	if int(request.COOKIES.get('visits')) > 30:
		resopnse = HttpResponse('cookies deleted')
		resopnse.delete_cookie('visits')
	else:
		resopnse = HttpResponse('cookie is less then 30')
	return resopnse


def createsession(request):
	request.session['name'] = 'user'
	request.session['password'] = 'user123'
	return HttpResponse('Created session')


def getsession(request):
	resopnse = "Welcome to session<br>"
	if request.session.get('name'):
		resopnse += "Name: {0} <br>".format(request.session.get('name'))
	if request.session.get('password'):
		resopnse += "password: {0} <br>".format(request.session.get('password'))
	return HttpResponse(resopnse)


def deletesession(request):
	try:
		del request.session['name']
		del request.session['password']
	except KeyError:
		pass
	return HttpResponse("Session data clear")

