from django.conf.urls import include, url
from useraccount import views

urlpatterns = [
    url(r'^$', views.indexView, name='index'),
    url(r'^sign_up$', views.signupView, name='sign_up'),
    url(r'^login$', views.loginView, name='login'),
    url(r'^logout$', views.logoutView, name='logout'),
    url(r'^forgot-password$', views.forgotPassswordView, name='forgot-password'),
    url(r'^reset-password$', views.resetPasswordView, name='reset-password'),
]