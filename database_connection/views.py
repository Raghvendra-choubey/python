# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    # request.
    return render(request, 'login.html')
