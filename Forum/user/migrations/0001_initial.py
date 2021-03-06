# Generated by Django 2.2.8 on 2020-04-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='头像')),
                ('sex', models.CharField(max_length=20, verbose_name='性别')),
                ('email', models.EmailField(max_length=100, verbose_name='邮箱')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生日期')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
