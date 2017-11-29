from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateForm 
from .models import User
# Create your views here.

def index(request):
    return render(request, 'diff/create.html')

def create(request):
    if request.method == 'POST':
	print "yes"
        form = CreateForm(request.POST,request.FILES)
	print form.is_valid()
        if form.is_valid():
            print "ok"
            form.save()
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
 
