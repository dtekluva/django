from django.conf.urls import include, url
from blog import views

urlpatterns = [
    url(r'^$', views.indexViews,name='blog-index'),
    url(r'^newsfeed/$', views.newsfeedViews,name='newsfeed'),
    url(r'^create-post/$', views.createPostView, name="create-post")
]