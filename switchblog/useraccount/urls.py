from django.conf.urls import include, url
from useraccount import views

urlpatterns = [
    url(r'^$', views.indexViews,name='user-index'),
    url(r'^user/sign-up$', views.signUpView,name='sign-up'),
    url(r'^user/login$', views.loginView,name='login'),
    url(r'^user/forgot-password$', views.forgotPasswordView,name='sign-up'),
    url(r'^user/reset-password$', views.resetPasswordView,name='reset-password'),
]
]