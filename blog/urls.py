from django.urls import path
from .views import AuthorView,AuthorBlogsView,authorBlogs

namespace='blog'
urlpatterns=[

path('details/<int:id>/',AuthorBlogsView,name='author-list'),
path('author/<int:id>',authorBlogs,name='author')
    ]