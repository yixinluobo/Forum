from django.db import models

from user.models import User


# 贴子
class Post(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容', null=True, blank=True)
    post_type = models.CharField('贴子类型', max_length=100)
    post_img = models.ImageField('贴子配图', upload_to='post_img/')
    create_time = models.DateTimeField('发表时间', auto_now=True)
    browse_nums = models.IntegerField('贴子浏览', default=0)
    # 外键
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='u_posts', verbose_name='作者')

    class Meta:
        verbose_name = '贴子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 贴子评论
class PostComment(models.Model):
    content = models.TextField('评论内容', null=True, blank=True)
    zan_nums = models.IntegerField('获赞', default=0)
    create_time = models.DateTimeField('评论时间', auto_now=True)
    # 外键
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='u_comments', verbose_name='评论者')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='p_comments', verbose_name='对应帖子')

    class Meta:
        verbose_name = '贴子评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


# 评论回复
class Reply(models.Model):
    content = models.TextField('回复内容')
    create_time = models.DateTimeField('回复时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='u_replies', verbose_name='回复者')
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name='c_replies', verbose_name='对应评论')

    class Meta:
        verbose_name = '评论回复'
        verbose_name_plural = verbose_name
