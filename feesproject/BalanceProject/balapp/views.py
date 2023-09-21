from django.shortcuts import render
from balapp.models import Balance
from balapp.forms import PayForm
from balapp.forms import SignUpForm
from django.http import HttpResponseRedirect
#from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required
def pay_fees(request):
    form=PayForm()
    if request.method=='POST':
        form=PayForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'balapp/feespay.html',{'form':form})

def list_view(request):
    bal_list=Balance.objects.all()
    return render(request,'balapp/list.html',{'bal_list':bal_list})

def log_out(request):
    return render(request,'balapp/logout.html')

def sign_up_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'balapp/signup.html',{'form':form})
