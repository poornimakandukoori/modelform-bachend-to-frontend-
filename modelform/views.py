from django.shortcuts import render
from modelform.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is d')
            
            
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage is d')

    return render(request,'insert_webpage.html',d)

def insert_AccessRecord(request):
    EARFO=AccessRecordform()
    d={'EARFO':EARFO}

    if request.method=='POST':
        ARFDO=AccessRecordform(request.POST)
        if ARFDO.is_valid():
            ARFDO.save()
            ARFDO=AccessRecord.objects.all()
            d={'AccessRecordform':ARFDO}
            return render(request,'display_Access.html',d)

    return render(request,'insert_AccessRecord.html',d)