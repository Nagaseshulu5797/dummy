from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def insert_data(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            ustd=tfd.save()

            uswd=wfd.save(commit=False)
            uswd.topic_name=ustd
            uswd.save()

            usad=afd.save(commit=False)
            usad.name=uswd
            usad.save()

            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data is not valid')







    return render(request,'insert_data.html',d)