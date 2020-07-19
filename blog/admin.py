from django.contrib import admin
from .models import Author, Blog
# Register your models here.

admin.site.register(Author)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['full_name','blog_name','created_at','modified_at']
admin.site.register(Blog,BlogAdmin)