from django.shortcuts import render, redirect
from django.http import HttpResponse
from useraccount.forms import UserAccountForm, UserRegistrationForm
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from useraccount.models import UserAccount
# Create your views here.

def indexView(request):
    return HttpResponse("You are at index")

def signupView(request):
    user_acc = UserAccountForm()
    user_form = UserRegistrationForm()
    #ensure user does not already exist
    if request.method=="POST":
        new_user=UserRegistrationForm(data=request.POST)
        if User.objects.filter(email = request.POST['email']).exists():
            messages.info(request,"sorry this email already exists")
            return redirect(reverse('useraccount:sign_up'))
        elif User.objects.filter(username=request.POST['username']).exists:
            messages.info(request, "sorry this username already exists")
            return redirect(reverse('useraccount:sign_up'))
        else:
            if user.is_valid():
                new_user = UserRegistrationForm(data=request.POST)
                new_uac = UserAccount.objects.create(user=new_user,occupation=request.POST['occupation'],phone=request.POST['phone'])
    return render(request, 'useraccount/signup.html', {'user_acc_form':user_acc,'user_form':user_form})

def loginView(request):
    return HttpResponse("You are at, The login module")

def forgotPassswordView(request):
    return HttpResponse("You are at, The forgotpassword module")

def resetPasswordView(request):
    return HttpResponse("You are at, The resetpassword module")
