from django import forms

from blog.models import Blog, Comment, Like, PostImage


class Blogform(forms.ModelForm):

    class Meta:
        model = Blog
        fields= ('title', 'body', 'category' )

