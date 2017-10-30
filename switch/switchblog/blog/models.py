from django.db import models
from useraccount.models import UserAccount

# Create your models here.
CATEGORY = (
    ('Ent', 'Entertainment'),
    ('Tech', 'Technology'),
    ('biz', 'Business'),
)
class PostImage(models.Model):
    image = models.FileField(upload_to="post/images")

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=2000)
    posted_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null = True)
    date_posted = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=125, choices=CATEGORY)
    is_fetched = models.BooleanField(default=False)
    source = models.CharField(max_length=75, null=True)
    images = models.ManyToManyField(PostImage)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    post_attached = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_by.user

class Like(models.Model):
    liked_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    post_attached = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.liked_by.user