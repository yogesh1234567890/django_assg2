from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import profile
from django.contrib.auth import get_user_model
from blog.models import Blog, Author
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profileView(request):
    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES, instance =request.user.profile )
        if form.is_valid():
            form.save()
            return redirect('profile_crud:dashboard')

    elif request.method=='GET':

        form=ProfileForm(instance=request.user.profile)

        context={
            'form':form
        }
        return render(request, 'html/profile.html',context)

@login_required(login_url='login')
def dashboardView(request):
    obj = Blog.objects.all()
    auth = Author.objects.all()
    name=request.user.profile.full_name


    return render(request,'html/dashboard.html',{'obj':obj,'auth':auth,'name':name})

