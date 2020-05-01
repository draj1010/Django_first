from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group
# Register your models here.

class ProductA(admin.ModelAdmin):
    # exclude = ('description', )
    list_display = ('name','description')

admin.site.register(Product,ProductA)
admin.site.unregister(Group)
admin.site.site_header = "Draj"