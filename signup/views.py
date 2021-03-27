from django.shortcuts import render,HttpResponse
from datetime import datetime
from signup.models import SignUp
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        signup = SignUp(name=name,email=email,password=password,date=datetime.today())
        signup.save()
        messages.success(request, 'Your data is saved!')
    return render(request, 'index.html')