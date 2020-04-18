from io import BytesIO

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from Forum.code import create_validate_code
from post.models import Post
from user.models import User


def check_code(request):
    """
    获取验证码
    :param request:
    :return:
    """
    stream = BytesIO()
    # 生成图片 img、数字代码 code，保存在内存中，而不是 Django 项目中
    img, code = create_validate_code()
    img.save(stream, 'PNG')

    # 写入 session
    request.session['valid_code'] = code
    print(code)
    return HttpResponse(stream.getvalue())


class LoginView(View):
    '''登录'''

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 获取表单信息
        params = request.POST.dict()
        username = params.get('username')
        password = params.get('password')
        # 获取用户输入的验证码
        code = params.get('confirm_code')
        # 用户输入的验证码与 session 中取出的验证码比较
        if code.upper() == request.session.get('valid_code').upper():
            # 验证码正确，验证用户名密码是否正确
            user = User.objects.filter(username=username, password=password)
            if len(user) <= 0:
                return JsonResponse({'msg': '用户名或密码错误'})
            else:
                # 登录成功存储记录
                user = user.first()
                user = model_to_dict(user)
                del user['photo']
                del user['birthday']
                request.session["LOGIN_LOCAL_FLAG"] = user
                return JsonResponse({'msg': '登录成功'})
        return JsonResponse({'msg': '验证码错误'})


class RegisterView(View):
    '''注册'''

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # 获取提交信息
        params = request.POST.dict()
        # 获取头像
        photo = request.FILES.get('image')
        params.setdefault('photo', photo)
        User.objects.create(**params)
        return redirect(to='/user/login')


def logout(request):
    '''
    退出登录
    :param request:
    :return:
    '''
    request.session.clear_expired()
    request.session.flush()
    return redirect(to="/")


def query(request):
    '''查询'''
    params = request.GET.dict()
    key = params.get('q')
    posts = Post.objects.filter(title__icontains=key)
    context = {
        'posts': posts,
    }
    return render(request, 'query.html', context)
