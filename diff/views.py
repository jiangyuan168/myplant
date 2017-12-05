from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import CreateForm,RegisterForm
from .models import User,InterfaceModel
import datetime
from django.views.generic import ListView
import json

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
    mock_data = {"count_test": "10", "count_online": "10", "diff_type": "url diff", "query": "%E5%B9%BF%E8%81%94%E8%BE%BE%E6%9C%8D%E5%8A%A1%E6%96%B0%E5%B9%B2%E7%BA%BF", "type": "top", "dis": "2-9,3-2,4-5,5-7,6-4,7-0,8-10,9-0,10-0,0-3,0-6,0-8"}
    mock_top = {"top10": 5.8499999999999996, "top9": 5.5999999999999996, "top8": 5.4000000000000004, "top7": 0000000000002, "top6": 3.9500000000000002, "top5": 3.5, "top4": 2.8999999999999999, "top3": 2.25, "top2": 1.5, "top1": 0.80000000000000004}
    mock_top_value = []
    mock_top_keylist = []
    for key in sorted(mock_top.iterkeys()):
        print "%s: %s" % (key, mock_top[key])
        mock_top_keylist.append(key)
        mock_top_value.append(mock_top[key])
    print mock_top_keylist
    print mock_top_value
    return render(request, 'diff/detail.html',context={'mock_data':mock_data,'mock_top_keylist':mock_top_keylist,'mock_top_value':mock_top_value}) 
