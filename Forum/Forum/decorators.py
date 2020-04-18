from functools import wraps
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.http import urlquote
from django.views import View

LOGIN_FLAG = "LOGIN_LOCAL_FLAG"


def auth_session(func):
    @wraps(func)
    def auth_session_wrapper(request, *args, **kwargs):
        if isinstance(request, View):  # 如果是CBV ,则 第一个参数是 View, 第二个参数才是request
            request = args[0]
        # 验证用户是否登录
        if not request.session.has_key(LOGIN_FLAG):
            return redirect(to='/user/login')

        # 如果 用户 登录了， 允许 访问 受保护的资源
        return func(request, *args, **kwargs)

    return auth_session_wrapper
