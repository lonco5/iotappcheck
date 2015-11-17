from django.shortcuts import render
from django.http import HttpResponse
import random 
from excuse.models import Excuse,Users
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

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

    try:
        if(p2 == Users.objects.get(NAME=p1).PW):
            return HttpResponse("pass")
        return HttpResponse("fail")
    except ObjectDoesNotExist:
        return HttpResponse("fail")

def registUser(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    p3 = request.GET.get('p3')
    p4 = request.GET.get('p4')

    try:
        Users.objects.create(
            NAME=p1,
            MAILBOX=p2,
            CELL=p3,
            PW=p4
            )
        return HttpResponse("pass")
    except IntegrityError:
        return HttpResponse("fail")

def updateUser(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    p3 = request.GET.get('p3')

    try:
        _target = Users.objects.get(NAME=p1)
        if(p2 == _target.PW):
            _target.PW = p3
            _target.save()
            return HttpResponse("pass")
        return HttpResponse("fail")
    except ObjectDoesNotExist:
        return HttpResponse("fail")
    except IntegrityError:
        return HttpResponse("fail")

# Create your views here.
