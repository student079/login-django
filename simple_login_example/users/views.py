from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def login(request):

    user_data = {
        'username': 'jjs',
        'password': 'jjs'
    }

    context = {
        'method': request.method,
        'is_valid': True
    }

    if (request.method == 'GET'):
        return render(request, 'users/login.html', context)

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # blank 상태일 때는, 유저가 input을 입력하지 않고 제출했을 때 (유저의 실수)
        if username == '':
            context['is_valid'] = False
        if password == '':
            context['is_valid'] = False

        if (username != user_data['username']):
            context['is_valid'] = False

        if (password != user_data['password']):
            context['is_valid'] = False

        if context['is_valid']:
            response = redirect('pages:index')

            response.set_cookie('username', user_data['username'])
            response.set_cookie('password', user_data['password'])
            response.set_cookie('is_login', True)

            return response

        return render(request, 'users/login.html', context)


def login_detail(request, id):
    return HttpResponse('user id 는' + str(id) + '입니다.')
