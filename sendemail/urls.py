# sendemail/urls.py
from django.contrib import admin
from django.urls import path, include

from .views import contactView, successView, edit_user
from .views import dashboard, register

urlpatterns = [
    path('', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('register/',register,name='register'),
    path('dashboard/', dashboard,name='dashboard'),
    path('edit_user/', edit_user,name='edit_user'),
    path('accounts/', include("django.contrib.auth.urls")),
]

