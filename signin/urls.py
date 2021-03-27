from django.urls import path,include
from signin import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("signin", views.signin, name = 'signin'),
path("signout", views.signout, name = 'signout')
]