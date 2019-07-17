from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse


def index(req):
    return HttpResponse('this is a welcome page')

def home(request):
    List = {}
    return render(request, 'app1/home.html', {'List': List})


# views.py
def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
