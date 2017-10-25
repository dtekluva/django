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
    if request.method == "POST":
        rp = request.POST
        print("==========step 1=============", rp)
     
        new_user = UserRegistrationForm(data = request.POST)
        if User.objects.filter(email = request.POST['email']).exists():
            print("==========step 2=======user already exists======", rp)
            messages.info(request,"sorry this email already exists")
            return redirect(reverse('useraccount:sign_up'))
        elif User.objects.filter(username = request.POST['username']).exists():
            print("==========step 3=======username already exists ======", rp)
            messages.info(request, "sorry this username already exists")
            return redirect(reverse('useraccount:sign_up'))
        else:
            print("==========step 4=======user does not exist ======", rp)
            if new_user.is_valid():
                
                
        
                new_user = User.objects.create(first_name=rp['first_name'], last_name=rp['last_name'],email=rp['email'],username=rp['username'])
                
                new_user.set_password(request.POST['password'])
                new_user.save()
                
                new_uac = UserAccount.objects.create(user=new_user,occupation=request.POST['occupation'],phone=request.POST['phone'])
                messages.info(request,"Registration successful")
            else:
                print("==========step 2=======user already exists======", new_user.errors)
    return render(request, 'useraccount/signup.html', {'user_acc_form':user_acc,'user_form':user_form})




def loginView(request):
    return HttpResponse("You are at, The login module")

def forgotPassswordView(request):
    return HttpResponse("You are at, The forgotpassword module")

def resetPasswordView(request):
    return HttpResponse("You are at, The resetpassword module")
