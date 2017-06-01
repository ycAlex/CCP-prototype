from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_session
from django.contrib.auth import logout as logout_session
from django.contrib.auth.models import User

from .models import Message


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        passwd = request.POST.get("password", "")
        user = authenticate(username=username, password=passwd)
        if user:
            login_session(request, user)
            return redirect("/message/")
    return render(request, "login.html")


def read_messages(request, fromuser):
    if not fromuser:
        fromuser = 0
    if request.user.is_authenticated():
        users = User.objects.all()
        message_re = Message.objects.filter(from_user=fromuser, to_user=request.user.id)
        message_se = Message.objects.filter(from_user=request.user.id, to_user=fromuser)

        messages = [i for i in message_re]
        messages.extend([i for i in message_se])
        messages = sorted(messages, key=lambda x: x.id)
        return render(request, 'message_read.html', {"user": request.user,
                                                     "users": users,
                                                     "messages": messages,
                                                     "fromuser": fromuser})


def index(request):
    if request.user.is_authenticated():
        users = User.objects.all()
        messages = []
        return render(request, 'message_read.html', {"user": request.user,
                                                     "users": users,
                                                     "messages": messages,
                                                     })
    else:
        return redirect('/message/login/')


def logout(request):
    logout_session(request)
    return redirect("/message/login/")


from datetime import datetime


def message_add(request, fromuser, touser):
    if request.method == "POST":
        content = request.POST.get("content", "")
        Message(from_user=fromuser, to_user=touser, create_time=datetime.now(),
                contents=content).save()
        return redirect("/message/sent/"+touser+'/')

def message_sent(request, touser):
    return render(request, 'message_sent.html', {'to': touser})
