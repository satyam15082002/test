from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Upload
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
# Create your views here.




def signup(request):
    if(request.method=='POST'):
        username=request.POST['username'].rstrip()
        pass1=request.POST['password1'].rstrip()
        pass2=request.POST['password2'].rstrip()
        email=request.POST['email'].rstrip()
        if User.objects.filter(username=username).exists():
            messages.info(request,"username taken by another")
            return redirect("signup")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken by another")
            return redirect("signup")
        else:
            if pass1==pass2:
                  user=User.objects.create_user(username=username,password=pass1,email=email)
                  user.save()
                  return render(request,'auth/signup.html',{"s":1})
            else:
                messages.info(request,"password not matching")
                return redirect("signup")

    else:
        return render(request,'auth/signup.html',{"s":0})

def login(request):
    if request.user.is_authenticated:
        return render(request,"auth/first.html",{"user":request.session.get('username')})
    else:
        if(request.method=='POST'):
                username=request.POST['username'].rstrip()
                password=request.POST['password'].rstrip()
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                     request.session['username']=username
                     auth.login(request,user)
                     return render(request,"auth/first.html",{"user":username})
                else:
                    messages.info(request,"inavlid credentials")
                    return redirect("login")
        else:
            return render(request,"auth/login.html")

@login_required(login_url="login")
def logout(request):
    request.session.flush()
    auth.logout(request)
    return render(request,"auth/login.html")

@login_required(login_url="login")
def home(request):
    a=Upload.objects.all().order_by('-id')
    parameter={"username":request.session.get('username'),"a":a}
    return render(request,"main/home.html",parameter)

@login_required(login_url="login")
def upload(request):
    parameter={"username":request.session.get('username')}
    if request.method=='POST':
        fn=request.FILES['img']
        uname=request.session['username']
        user=User.objects.get(username=uname)
        u=Upload(user=user,username=uname,img=fn)
        u.save()
        messages.info(request,"file uploaded successfully")
        return redirect("upload")
    else:
        return render(request,"main/upload.html",parameter)

@login_required(login_url="signup")
def  delete(request):
    if request.method=='POST':
            name=request.session.get('username')
            u=User.objects.get(username=name)
            up=u.upload.all()
            for i in up:
                path=str(i.img)
                img_name=path.split('/')
                apath=os.getcwd()+"\\media\\pics\\"+img_name[-1]
                os.remove(apath)
            u.delete()
            auth.logout(request)
            request.session.flush()
            return render(request,"auth/signup.html")

@login_required(login_url="login")
def setting(request):
    parameter={"username":request.session.get('username')}
    return render(request,'main/setting.html',parameter)


