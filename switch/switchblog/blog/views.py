from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexViews(request):
    return HttpResponse("You are at, The blog module")

