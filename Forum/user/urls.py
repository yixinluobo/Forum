from django.urls import path

from user import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    # 获取验证码
    path('check_code/', views.check_code, name='check_code'),
    path('logout', views.logout, name='logout'),
    path('query', views.query, name='query'),
]
