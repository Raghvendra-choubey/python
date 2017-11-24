# Create your views here.

from django.shortcuts import render

from database_connection.models import Users


def index(request):
    return render(request, 'index.html')


'''
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
'''

def login(request):
    # request.
    u_name = request.POST.get("u_name")
    id_password = request.POST.get("id_password")

    # print("u_name", u_name)
    # print("password", id_password)
    # print("select COUNT(*) as c_count from UserDetails where userterms ='" + u_name + "'")
    '''cursor = connection.cursor()
    cursor.execute("select COUNT(*) as c_count from sysmmsuser where id ='" + u_name + "' and password='"+id_password+"'")
    results = namedtuplefetchall(cursor)
    if results[0].c_count >= 1:
        dict = {'user': u_name}
        return render(request, 'home.html', {'dict': dict})
    else:
        return render(request, 'index.html')
    '''
    login_user = Users.objects.filter(id=u_name, trans_flag='A')
    if login_user.__len__() > 0:
        login_user_password = login_user[0].password
        print(login_user_password)
        print(id_password)
        if login_user_password.upper().strip() == id_password.upper().strip():
            # dict = {'user': u_name}
            return render(request, 'home.html', {'dict': {'user': u_name}})
        else:
            return render(request, 'index.html', {'dict': {'message': 'ID & Password do not match.'}})
    else:
        return render(request, 'index.html', {'dict': {'message': 'User does not exist or deactivated.'}})


def create_user(request):
    # request
    print("hello")
