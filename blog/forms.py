from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields=['blog_name','blog_content']

class BlogForms(ModelForm):
    class Meta:
        model = Blog
        fields="__all__"