#-*- coding:utf-8 -*- 
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50)

    class Meta(AbstractUser.Meta):
        pass


class InterfaceModel(models.Model):
    QUERY_NUM = (
        ('50',50),
        ('100',100),
        ('300',300),
        ('500',500),
        ('1000',1000),
        ('2000',2000),
        ('3000',3000),
        ('5000',5000),
        ('10000',10000),
    )
    TOP_NUM = (
        ('1',1),
        ('3',3),
        ('5',5),
        ('10',10),
        ('20',20),
    )
    PN_NUM = (
        ('1',1),
        ('2',2),
        ('3',3),
        ('4',4),
        ('5',5),
    )
    REPEAT_NUM =(
        ('1',1),
        ('2',2),
        ('3',3),
        ('5',5),
    )
    THREAD_NUM = (
        ('1',1),
        ('2',2),
        ('3',3),
        ('5',5),
    )
    REASON = (
        ('YES','Y'),
        ('NO','N'),
    )    
    testurl = models.CharField(max_length=300)
    defaulturl = models.CharField(max_length=300)
    querycount = models.CharField(max_length=10,choices=QUERY_NUM,default='50')
    topn  = models.CharField(max_length=10,choices=TOP_NUM,default='10')
    pn = models.CharField(max_length=10,choices=PN_NUM,default='1')
    countrepeat = models.CharField(max_length=10,choices=REPEAT_NUM,default='3')
    statusflag = models.CharField(max_length=50)
    resultflag = models.CharField(max_length=50)
    threadnum = models.CharField(max_length=10,choices=THREAD_NUM,default='5')
    reason = models.CharField(max_length=5,choices=REASON,default='NO')
    remark = models.TextField()
    selfdata = models.FileField(upload_to='./upload/')

