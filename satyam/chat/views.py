from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from .models import Group,Message
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def create(request):
    parameter={"username":request.session.get("username")}
    return render(request,"chat/create.html",parameter)
    
@login_required(login_url="login")    
def create_group(request):
    group_name=request.POST["group_name"]
    user=User.objects.get(username=request.session.get("username"))
    g=Group(group_name=group_name,admin=request.session.get("username"))
    g.save()
    g.memeber.add(user)
    g.save()
    messages.info(request,"created successfully")
    return redirect("create")

@login_required(login_url="login")
def home(request):
    user=User.objects.get(username=request.session.get("username"))
    group=user.group.all()
    parameter={"group":group,"username":request.session.get("username")}
    return render(request,"chat/home.html",parameter)

@login_required(login_url="login")
def ingroup(request,id):
    group=Group.objects.get(id=id)
    msg=group.message.all()
    uname=request.session.get("username")
    admin=False
    if group.admin==uname:
        admin=True
    request.session["count"]=group.message.all().count()
    parameter={"group":group,"username":request.session.get("username"),"msg":msg,"admin":admin}
    return render(request,"chat/insidegroup.html",parameter)

@login_required(login_url="login")
def search(request):
    g=Group.objects.all().order_by('-id')
    parameter={"group":g,"username":request.session.get("username")}
    return render(request,"chat/search.html",parameter)

@login_required(login_url="login")
def add(request,group_id):
    user=User.objects.get(username=request.session.get("username"))
    group=Group.objects.get(id=group_id)
    group.memeber.add(user)
    group.save()
    return redirect("search")

@login_required(login_url="login")
def addmsg(request,g_id):
    msg=request.GET["message"]
    group=Group.objects.get(id=g_id)
    m=Message(name=request.session.get("username"),msg=msg,grp=group)
    m.save()
    return HttpResponse("hello")

@login_required(login_url="login")
def loadmsg(request,g_id):
    group=Group.objects.get(id=g_id)
    count=group.message.all().count()
    msg=group.message.all().order_by('-id')
    txt=""
    for m in msg:
        txt=f"<li>{m.name}::-{m.msg}</li>"+txt
    if(request.session.get("count")!=count):
        request.session["count"]=count
        return HttpResponse(txt)
    else:
        return HttpResponse("")

@login_required(login_url="login")
def delete(request,g_id):
    g=Group.objects.get(id=g_id)
    g.delete()
    return redirect("home")