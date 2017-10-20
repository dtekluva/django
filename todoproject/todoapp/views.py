from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<button>Hello World</button>')
# Create your views here.
