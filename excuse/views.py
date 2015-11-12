from django.shortcuts import render
from django.http import HttpResponse
import random 
from excuse.models import Excuse

def home(request):
    excuses = [
        "It was working in my head",
        "I thought I fixed that",
        "Actually, that is a feature",
        "It works on my machine",
    ]

    excuse = random.choice(Excuse.objects.all())
    return HttpResponse(excuse)


 
def helloParams(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    users = {
    'iot': 'iot', 
    'smartlife': 'smartlife'
    };
    if(p1 in users):
    	if p2 == users[p1]:
    		return HttpResponse("pass")
    return HttpResponse("fail")

# Create your views here.
