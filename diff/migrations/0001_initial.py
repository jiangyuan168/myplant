# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=50, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='InterfaceModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.IntegerField(default=1)),
                ('testurl', models.CharField(max_length=300)),
                ('defaulturl', models.CharField(max_length=300)),
                ('querycount', models.CharField(default=b'50', max_length=10, choices=[(b'50', 50), (b'100', 100), (b'300', 300), (b'500', 500), (b'1000', 1000), (b'2000', 2000), (b'3000', 3000), (b'5000', 5000), (b'10000', 10000)])),
                ('topn', models.CharField(default=b'10', max_length=10, choices=[(b'1', 1), (b'3', 3), (b'5', 5), (b'10', 10), (b'20', 20)])),
                ('pn', models.CharField(default=b'1', max_length=10, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'4', 4), (b'5', 5)])),
                ('countrepeat', models.CharField(default=b'3', max_length=10, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'5', 5)])),
                ('statusflag', models.CharField(max_length=50)),
                ('resultflag', models.CharField(max_length=50)),
                ('threadnum', models.CharField(default=b'5', max_length=10, choices=[(b'1', 1), (b'2', 2), (b'3', 3), (b'5', 5)])),
                ('reason', models.CharField(default=b'NO', max_length=5, choices=[(b'YES', b'Y'), (b'NO', b'N')])),
                ('remark', models.TextField()),
                ('upload', models.BooleanField(default=False)),
                ('selfdata', models.FileField(upload_to=b'./upload/', blank=True)),
                ('creater', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
