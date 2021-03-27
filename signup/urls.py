from django.contrib import admin
from django.urls import path,include
from signup import views

urlpatterns = [
    path("", views.index, name = 'index'),
path("signup", views.signup, name = 'signup')
]
