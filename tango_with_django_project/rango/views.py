from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    
    #context_dict = {'boldmessage': "I am bold font from the context"}
    category_list = Category.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/index.html', context_dict)    

def category(request, category_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(Category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    return render(request, 'rango/category.html', context_dict)

def about(request):
   
    message = {'boldmessage':"You are welcome to play with rango",'second':"/rango/images/2.webp", 'third':"And then the great Django shall appear"}
    return render(request, 'rango/about.html')
# Create your views here.

def lorem(request):
    message = {'boldmessage':"You are welcome to play with rango",'second':"Rango image would soon be here", 'third':"And then the great Django shall appear"}
    return render(request, 'rango/lorem.html', message)
# Create your views here.
