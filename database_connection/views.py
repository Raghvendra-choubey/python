# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    # request.
    u_name = request.GET.get("u_name")
    id_password = request.GET.get("id_password")

    print("u_name", u_name)
    print("password", id_password)
    return render(request, 'login.html')
