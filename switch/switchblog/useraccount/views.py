from django.shortcuts import render
from django.http import HttpResponse
from useraccount.forms import UserAccountForm, UserRegistrationForm
# Create your views here.

def indexView(request):
    return HttpResponse("You are at index")

def signupView(request):
    user_acc = UserAccountForm()
    user_form = UserRegistrationForm()

    return render(request, 'useraccount/signup.html', {'user_acc_form':user_acc,'user_form':user_form})

def loginView(request):
    return HttpResponse("You are at, The login module")

def forgotPassswordView(request):
    return HttpResponse("You are at, The forgotpassword module")

def resetPasswordView(request):
    return HttpResponse("You are at, The resetpassword module")