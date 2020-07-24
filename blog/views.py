from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Author,Blog
from .forms import BlogForm,BlogForms

@login_required(login_url='login')
def authorBlogs(request,id):
    user_obj = Blog.objects.filter(id=id)
    return render(request, 'detail.html', context={
        'user_obj': user_obj
    })

@login_required(login_url='login')
def BlogsUpdate(request,id):
    object=get_object_or_404(Blog, id=id)
    if request.method=="POST":
        form = BlogForm(request.POST,instance=object)
        if form.is_valid():
            form.save()
            return redirect('profile_crud:dashboard')
        else:
            raise ValueError("The form is invalid")
    else:
        form = BlogForm(instance=object)
    return render(request,"UpdateForm.html",{
        'form':form
    })

@login_required(login_url='login')
def BlogsCreate(request):
    if request.method=="POST":
        form = BlogForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_crud:dashboard')
        else:
            raise ValueError("The form is invalid")
    else:
        form = BlogForms()
    return render(request,"CreateForm.html",{
        'form':form
    })