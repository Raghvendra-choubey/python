# Create your views here.
from collections import namedtuple

from django.db import connection
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def login(request):
    # request.
    u_name = request.GET.get("u_name")
    id_password = request.GET.get("id_password")

    print("u_name", u_name)
    print("password", id_password)
    print("select COUNT(*) as c_count from UserDetails where userterms ='" + u_name + "'")
    cursor = connection.cursor()
    cursor.execute("select COUNT(*) as c_count from UserDetails where userterms ='" + u_name + "'")
    results = namedtuplefetchall(cursor)
    print(results[0].c_count)
    return render(request, 'login.html')
