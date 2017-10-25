from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/index.html', context_dict)    


def about(request):
   
    message = {'boldmessage':"You are welcome to play with rango",'second':"/rango/images/2.webp", 'third':"And then the great Django shall appear"}
    return render(request, 'rango/about.html')
# Create your views here.

def lorem(request):
    message = {'boldmessage':"You are welcome to play with rango",'second':"Rango image would soon be here", 'third':"And then the great Django shall appear"}
    return render(request, 'rango/lorem.html', message)
# Create your views here.
