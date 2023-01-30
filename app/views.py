from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html')

def insert_webpages(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=='POST':
        topic=request.POST.get('topic')
        na=request.POST['na']
        ur=request.POST.get('ur')
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpages.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('insert_webpages is created')
    return render(request,'insert_webpages.html',d)

def insert_Access(request):
    QSW=Webpages.objects.all()
    d={'webpages':QSW}
    if request.method=='POST':
        name=request.POST['na']
        date=request.POST.get('dt')
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpages.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=dt)[0]
        A.save()
        
        return HttpResponse('insert_Access is created')
    return render(request,'insert_Access.html',d)