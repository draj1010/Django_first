from django.shortcuts import render
from mysite.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.core.files.storage import FileSystemStorage
from .forms import EmailForm
# Create your views here.
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == "POST":
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to mysite'
        message = 'this is a test message'
        recepient = str(sub['Email'].value())
        message_admin = 'hey you have new subscriber ' + str([recepient])
        mail_admin = str(EMAIL_HOST_USER)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        send_mail('New subscriber', message_admin, EMAIL_HOST_USER, [mail_admin], fail_silently = False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})

def demo(request):
    message1 = ('Subject here', 'Here is the message', EMAIL_HOST_USER, ['ehl52090@zzrgg.com', 'dgh94777@bcaoo.com'])
    message2 = ('Another Subject', 'Here is another message', EMAIL_HOST_USER, ['drajyadav1010@gmail.com'])
    send_mass_mail((message1, message2), fail_silently=False)
    return render(request, 'index.html')

def email(request):
    if request.method == "POST":
        form = EmailForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            document = request.FILES.get('document')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            email = EmailMessage(subject,message,email_from,recipient_list)
            base_dir = 'media/documents/'
            email.attach_file('media/documents/'+str(document))
            email.send()
        else:
            form = EmailForm()
        return render(request, 'sendemail.html', {'form': form})