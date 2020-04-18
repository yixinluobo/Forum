from django.db import models


# Create your models here.
# 用户
class User(models.Model):
    username = models.CharField('用户名', max_length=100)
    password = models.CharField('密码', max_length=100)
    photo = models.ImageField('头像', upload_to='photo/')
    sex = models.CharField('性别', max_length=20)
    email = models.EmailField('邮箱', max_length=100)
    birthday = models.DateField('出生日期', blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
