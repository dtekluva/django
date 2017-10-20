from django.db import models
from useraccount.models import UserAccount

# Create your models here.
CATEGORY=(
    ('ENTERTAINMENT','ENTERTAINMENT',),
    ('BIZ','BUSINESS',),
    ('TECH','TECHNOLOGY',),
    )

class PostImage(models.Model):
        image=models.FileField(upload_to='post/image')

class Blog(models.Model):
    title       = models.CharField(max_length=255)
    body        = models.TextField(max_length=2000)
    post_by     = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)
    category    = models.CharField(max_length=125,choices=CATEGORY)
    is_fetched  = models.BooleanField(default=False)
    source      = models.CharField(max_length=75,null=True)
    Images      = models.ManyToManyField(PostImage)

    def __unicode__(self):
        return self.title

    
class Comment(models.Model):
    comment_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500)
    post_attached=models.ForeignKey(Blog , on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_now=True)

    def __unicode(self):
        return self.comment_by.user

class Comment(models.Model):
    liked_by = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    post_attached=models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_liked=models.DateTimeField(auto_now=True)

    def __unicode(self):
        return self.liked_by.user