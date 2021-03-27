from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    return render(request, "index.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/signin")

    messages.success(request, 'Your are Logged In!')


def signout(request):
    logout(request)
    return redirect("/signin")