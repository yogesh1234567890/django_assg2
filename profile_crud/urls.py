from django.urls import path
from .views import profileView,dashboardView

app_name='profile_crud'

urlpatterns=[
path('',profileView, name='profile'),
path('dashboard/',dashboardView, name='dashboard')
]