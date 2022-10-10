from django.shortcuts import render
from .forms import Login_form
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import Signup


def login_view(request):
    form=Login_form()

    if request.method=='POST':
        form = Login_form(request.POST)
        #Loading the submitted data to the file
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user = authenticate(request,username=username,password=password)

            if user:
                login(request,user)
                return HttpResponseRedirect('/list/')

    td={'form':form}
    return render(request,'login.html',td)

def signup(request):
    sign=Signup()

    if request.method=='POST':
        form = Signup(request.POST)
        #Loading the submitted data to the file
        if form.is_valid():
            First_name=form.cleaned_data['First_name']
            Last_name = form.cleaned_data['Last_name']
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user = User.objects.create_user(username=username,password=password,first_name=First_name,last_name=Last_name)
            return HttpResponseRedirect('/login/')

    a={'form':sign}
    return render(request,'signup.html',a)
# Create your views here.
