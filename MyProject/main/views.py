from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def katha(request):
    return render(request, 'katha.html')


def shokseva(request):
    return render(request, 'shokseva.html')


def birthday(request):
    return render(request, 'birthday.html')


def signup_login(request):
    return render(request, 'signup_login.html')


def wedding(request):
    return render(request, 'wedding.html')


def team(request):
    return render(request, 'team.html')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile_no = request.POST['mobile_no']
        email = request.POST['email']
        message = request.POST['message']

        user = User(name=name, mobile_no=mobile_no, email=email, message=message)
        user.save()

    return render(request, 'index.html')
