from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def january(request):
    return HttpResponse("This is the challenge for january!")

def february(request):
    return HttpResponse("This is the challenge for february!")