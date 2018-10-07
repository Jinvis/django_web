# coding:utf-8

# Create your views here.
from .getFiles import getfiles
from django.http import HttpResponse
from django.shortcuts import render
import os
from .models import VideoInfo


def index(request):
    filepath  = os.path.dirname(__file__)
    videolist = getfiles(filepath + "\\.." + "\\static\\video")
    return render(request, 'teco_home.html', {'videolist': videolist})


def video(request, name):
    return render(request, 'video_page.html', {'videoname': name})


#def getform(request):
#    user_msg = UserMessage()
#    user_msg.name = 'xjin'
#    user_msg.message = 'hello world'
#    user_msg.email = 'aa@163.com'
#    user_msg.address = 'sh'
#    user_msg.save()
#    return render(request, 'teco_home.html')
