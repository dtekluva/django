from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import Blogform

from blog.models import PostImage
# Create your views here.

def indexViews(request):
    return render(request, 'index.html',{})

def newsfeedViews(request):
    return render(request, 'base.html',{})

def createPostView(request):
    article_form = Blogform()
    context      = {'article_form':article_form}

    if request.method == "POST":
        post_form          = Blogform(data = request.POST)
        new_post = post_form.save()
        post_image         = PostImage.objects.create(image = request.FILES['post_image'])
        new_post.images.add(post_image)
        new_post.posted_by= request.user.useraccount
        new_post.save()

    return render(request, 'create-post.html', context)