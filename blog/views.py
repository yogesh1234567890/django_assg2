from django.shortcuts import render,get_object_or_404
from .models import Author,Blog

def AuthorView(request):
    data=Author.objects.all()
    context={
        'data':data
    }
    return render(request,'index.html',context)

def AuthorBlogsView(request, id):
    obj = Blog.objects.filter(full_name_id=id)
    return render(request,'AuthorDetails.html',context={'obj':obj})



def authorBlogs(request,id):
    user_obj = Blog.objects.filter(id=id)
    return render(request, 'detail.html', context={
        'user_obj': user_obj
    })
