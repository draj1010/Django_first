from django.shortcuts import render
from . import forms

# Create your views here.
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we recieved this form again'
        if form.is_valid():
            html = html + "form is valid"
    else:
        html = 'welcome for first time'
    return render(request, 'signup.html', {'html':html, 'form':form})