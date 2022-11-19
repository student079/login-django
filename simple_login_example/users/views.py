from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    user_data = {
        'username': 'jjs',
        'password': 'jjs'
    }

    if (request.method == 'GET'):
        return render(request, 'users/login.html')

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # blank 상태일 때는, 유저가 input을 입력하지 않고 제출했을 때 (유저의 실수)
        if username == '':
            return HttpResponse('유저 아이디를 입력해주세요')
        if password == '':
            return HttpResponse('유저 비밀번호를 입력해주세요')

        if (username != user_data['username']):
            return HttpResponse('유저 아이디가 올바르지 않습니다.')

        if (password != user_data['password']):
            return HttpResponse('유저 비밀번호가 올바르지 않습니다.')

        return HttpResponse('로그인 성공!')


def login_detail(request, id):
    return HttpResponse('user id 는' + str(id) + '입니다.')
