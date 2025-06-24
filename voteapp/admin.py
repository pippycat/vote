from django.contrib import admin
from .models import Category, CategoryItem


# Register your models here.

class Categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
    
admin.site.register(Category, Categoryadmin)
admin.site.register(CategoryItem)