from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from Forum import code
from Forum.decorators import auth_session
from post.models import Post, PostComment, Reply
from user.models import User


class PublicPostView(View):
    '''发帖'''

    @auth_session
    def get(self, request):
        return render(request, 'pub_post.html')

    @auth_session
    def post(self, request):
        params = request.POST.dict()
        image = request.FILES.get('post_img')
        user_id = code.get_current_user_id(request)
        user = User.objects.get(pk=user_id)
        params.setdefault('post_img', image)
        params.setdefault('user', user)
        Post.objects.create(**params)
        return redirect(to='/')


class PostDetailView(View):
    '''贴子详情'''

    def get(self, request, pk):
        # 贴子id
        post = Post.objects.get(pk=pk)
        user = post.user
        comments = PostComment.objects.filter(post=post)
        # 增加浏览量
        post.browse_nums += 1
        post.save()
        # 评论回复
        replies = Reply.objects.all().order_by('-create_time')
        context = {
            'post': post,
            'user': user,
            'comments': comments,
            'replies': replies,
        }
        return render(request, 'detail.html', context)


class PostCommentView(View):
    '''贴子评论'''

    def get(self, request, post_id):
        '''点赞'''
        comment = PostComment.objects.get(pk=post_id)
        zan_nums = comment.zan_nums + 1
        comment.zan_nums = zan_nums
        comment.save()
        return JsonResponse({'msg': '点赞成功'})

    @auth_session
    def post(self, request, post_id):
        params = request.POST.dict()
        user_id = code.get_current_user_id(request)
        user = User.objects.get(pk=user_id)
        post = Post.objects.get(pk=post_id)
        params.setdefault('user', user)
        params.setdefault('post', post)
        PostComment.objects.create(**params)
        return JsonResponse({'msg': '评论成功'})


class ReplyView(View):
    '''回复评论'''

    @auth_session
    def post(self, request):
        params = request.POST.dict()
        comment_id = params.get('comment_id')
        comment = PostComment.objects.get(pk=comment_id)
        user_id = code.get_current_user_id(request)
        user = User.objects.get(pk=user_id)
        params.setdefault('user', user)
        params.setdefault('comment', comment)
        del params['comment_id']
        Reply.objects.create(**params)
        return JsonResponse({'msg': '回复成功'})
