from django.db import models
from django.utils import timezone

class Author(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    full_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=100)
    blog_content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
