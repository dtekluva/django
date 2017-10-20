from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexViews(request):
    return HttpResponse("You are at, The useraccount module")

def signUpView(request):
    pass
    #return HttpResponse("You are at, The api module")

def loginView(request):
    pass
    #return HttpResponse("You are at, The api module")

def forgotPasswordView(request):
    pass
    #return HttpResponse("You are at, The api module")

def resetpasswordView(request):
    pass
    #return HttpResponse("You are at, The api module")