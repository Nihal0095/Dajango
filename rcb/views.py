from django.shortcuts import render
from django.template import loader
from . models import TeamDetails

# Create your views here.
from django.http import HttpResponse
def teamdetails(request):
    return HttpResponse("team of 12 players ,RCB ")
    

def display(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render())

#create a views and templates fgor modelsm

def myplayer_list(request):
    myplayers=TeamDetails.object.all()
    return render(request, 'mymodel_list.html', {'myplayer': myplayers})
