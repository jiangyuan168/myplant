from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import CreateForm,RegisterForm
from .models import User,InterfaceModel
import datetime
from django.views.generic import ListView
# Create your views here.

def index(request):
    return render(request, 'diff/tables-1.html')

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
   return render(request, 'diff/detail.html') 
