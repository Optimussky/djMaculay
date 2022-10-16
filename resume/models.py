from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Resume(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Nacionality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30, default='Avaliable')
    Address = models.CharField(max_length=30)
    Phone = models.CharField(max_length=12)
    Email = models.CharField(max_length=30)
    Skype = models.CharField(max_length=30)
    Languages = models.CharField(max_length=30)

    def __str__(self):
        return self.First_Name

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.title
