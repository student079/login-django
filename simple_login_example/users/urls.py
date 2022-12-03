from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),  # users/login/,
    path('login/<int:id>/', views.login_detail, name='login-detail'),
    path('login/index', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup')
]
