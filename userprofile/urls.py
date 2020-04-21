from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户注册
    path('register/', views.user_register, name='register'),
]