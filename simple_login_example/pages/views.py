from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def index(request: HttpRequest):
    """
    페이지만 호풀하니까 if request.method == "GET"생략 가능
    """
    context = {
        "is_login": False,
        "username": None,
        "password": None
    }

    is_login = request.COOKIES.get('is_login')
    if is_login:
        context['is_login'] = True
        context['username'] = request.COOKIES['username']
        context['password'] = request.COOKIES['password']

    return render(request, 'index.html', context)
