from django.contrib import admin

# Register your models here.
from .models import Userx, todo

admin.site.register(Userx)
admin.site.register(todo)