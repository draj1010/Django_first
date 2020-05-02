from django.contrib import admin
from .models import Product,Category
from django.contrib.auth.models import Group
# Register your models here.

def change_rating(modeladmin,request,queryset):
    queryset.update(rating = 'e')

change_rating.short_description = "Rate Excellent"

class ProductA(admin.ModelAdmin):
    # exclude = ('description', )
    list_display = ('name','description','rating','mfg_date','catagory')
    list_filter = ('mfg_date',)
    actions = [change_rating]

admin.site.register(Product,ProductA)

class CategoryA(admin.ModelAdmin):
    list_display = ('cat_name','parent','slug')

admin.site.register(Category,CategoryA)
# admin.site.unregister(Group)
admin.site.site_header = "Draj"