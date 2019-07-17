from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def add(request):

    c = 0
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def index(request):
    return render(request, 'home.html')

def old_add2_redirect(request, a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
    )