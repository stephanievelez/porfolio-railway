"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users' #helps Django distinguish this urls.py file from files of the same name in other apps within the project ie localhost:8000/users/login
urlpatterns = [
    #Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    #Logout page
    path('logout/', views.logout_view, name='logout'),

    #Registration page
    path('register/', views.register, name='register'),
]