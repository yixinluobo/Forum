from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from post.models import Post


def home(request):
    return redirect(to='/ ')


def index(request, post_type):
    '''首页'''
    # 最新帖子
    new_posts = Post.objects.all().order_by('-create_time')[0:10]
    # 贴子列表
    if post_type == ' ':
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(post_type=post_type)
    context = {
        'new_posts': new_posts,
        'posts': posts,
    }
    return render(request, 'index.html', context)
