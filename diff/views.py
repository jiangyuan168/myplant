from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import CreateForm,RegisterForm
from .models import User,InterfaceModel
import datetime
from django.views.generic import ListView
import json
import re
# Create your views here.

def index(request):
    return render(request, 'diff/test.html')

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST,request.FILES)
	print form.is_valid()
        if form.is_valid():
            print "ok"
            task_info = form.save(commit=False)
            task_info.creater = request.user.username
            task_info.create_time = datetime.datetime.now()
            if task_info.selfdata :
                task_info.upload = True
            else:
                task_info.upload = False
            print task_info.create_time
            task_info.save()
            return redirect('/')
        else:
            errorinfo = form.errors.as_data()
            print "form invalid"
            print errorinfo
    else:
        print "faile"
	print "POST:%s" %(request.method) 
        form = CreateForm()
    return render(request,'diff/create.html',context={'form':form})


def register(request):
    redirect_to = request.POST.get('next',request.GET.get('next',''))
    print "redirect_to:%s" %(redirect_to)
    if request.method == 'POST':
        form =  RegisterForm(request.POST)
        print "register"
        print form
        print form.is_valid()
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        print "up"
        form = RegisterForm()
    return render(request,'diff/register.html',context={'form':form,'next':redirect_to})

#def channel(request,cid):
#    #channel_data = get_object_or_404(InterfaceModel,cid=cid).order_by('-create_time')
#    channel_list = InterfaceModel.objects.all().order_by('-create_time')
#    print channel_list
#    return render(request,'diff/channel.html',context={'channel_list':channel_list})

class ChannelView(ListView):
    model = InterfaceModel
    template_name = 'diff/channel.html'
    context_object_name = 'channel_list'
    def get_queryset(self):
        channel_list = InterfaceModel.objects.all().order_by('-create_time')
        return super(ChannelView,self).get_queryset().filter(cid=self.kwargs.get('cid'))



def detail(request):
    diff_result_list = {"count_test": "10", "count_online": "10", "diff_type": "url diff", "query": "%E5%B9%BF%E8%81%94%E8%BE%BE%E6%9C%8D%E5%8A%A1%E6%96%B0%E5%B9%B2%E7%BA%BF", "type": "top", "dis": "2-9,3-2,4-5,5-7,6-4,7-0,8-10,9-0,10-0,0-3,0-6,0-8"}
    diff_top = {"top10": 5.8499999999999996, "top9": 5.5999999999999996, "top8": 5.4000000000000004, "top7": 0000000000002, "top6": 3.9500000000000002, "top5": 3.5, "top4": 2.8999999999999999, "top3": 2.25, "top2": 1.5, "top1": 0.80000000000000004}
    wenda_so_influence = {u'\u6d4b\u8bd5\u73af\u5883\u5360\u6bd4\u66f4\u9ad8': 28, u'\u4e24\u4e2a\u73af\u5883\u5360\u6bd4\u76f8\u540c': 72, u'\u7ebf\u4e0a\u73af\u5883\u5360\u6bd4\u66f4\u9ad8': 17}
    zhidao_baidu_influence = {u'\u6d4b\u8bd5\u73af\u5883\u5360\u6bd4\u66f4\u9ad8': 3, u'\u4e24\u4e2a\u73af\u5883\u5360\u6bd4\u76f8\u540c': 97, u'\u7ebf\u4e0a\u73af\u5883\u5360\u6bd4\u66f4\u9ad8': 17}
    baike_so_influence = {u'\u6d4b\u8bd5\u73af\u5883\u5360\u6bd4\u66f4\u9ad8': 15, u'\u4e24\u4e2a\u73af\u5883\u5360\u6bd4\u76f8\u540c': 82, u'\u7ebf\u4e0a\u73af\u5883\u5360\u6bd4\u66f4\u9ad8': 20}
    baike_baidu_influence = {u'\u6d4b\u8bd5\u73af\u5883\u5360\u6bd4\u66f4\u9ad8': 16, u'\u4e24\u4e2a\u73af\u5883\u5360\u6bd4\u76f8\u540c': 101, u'\u7ebf\u4e0a\u73af\u5883\u5360\u6bd4\u66f4\u9ad8': 0}
    diff_classified_dict = {u'url diff': 115, u'content diff': 1, u'count diff': 1}
    query_classified_dict = {u'ads': 10, u'medical': 6, u'spam': 8, u'top': 19, u'rewrite': 9, u'telephone': 1, u'wenda': 14, u'sensitive': 3, u'hot': 8, u'diyu': 13, u'zhida': 2, u'baike': 24}
    diff_top_value = []
    diff_top_keylist = []
    diff_top_keylist = diff_top.keys()
    diff_top_keylist.sort(key = lambda x:int(re.match('top(\d+)',x).group(1)))
    for key in diff_top_keylist:
        print "%s: %s" % (key, diff_top[key])
        diff_top_value.append(diff_top[key])

    print diff_top_keylist
    print diff_top_value
    return render(request, 'diff/detail.html',context={'diff_result_list':diff_result_list,
                                                       'diff_top_keylist':diff_top_keylist,
                                                       'diff_top_value':diff_top_value,
                                                       'diff_classified_dict':diff_classified_dict,
                                                       'query_classified_dict':query_classified_dict,
                                                       'wenda_so_influence':wenda_so_influence,
                                                       'zhidao_baidu_influence':zhidao_baidu_influence,
                                                       'baike_so_influence':baike_so_influence,
                                                       'baike_baidu_influence':baike_baidu_influence,
                                                   })
 
