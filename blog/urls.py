from django.urls import path
from .views import authorBlogs,BlogsUpdate,BlogsCreate

namespace='blog'
urlpatterns=[

path('author/<int:id>',authorBlogs,name='author'),
path('update/<int:id>',BlogsUpdate,name="update"),
path('create/',BlogsCreate,name="create")

    ]