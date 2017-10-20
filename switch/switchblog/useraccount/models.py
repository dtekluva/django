from django.db import models 

# Create your models here.
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.OneToOneField(User)
    occupation = models.CharField(max_length=256)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user