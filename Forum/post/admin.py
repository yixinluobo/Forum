from django.contrib import admin
from .models import Post, PostComment, Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'post_type', 'post_img', 'create_time')
    # 满50条数据就自动分页
    list_per_page = 50
    # 后台数据列表排序方式
    ordering = ('-create_time',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'zan_nums', 'create_time')


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'create_time')
