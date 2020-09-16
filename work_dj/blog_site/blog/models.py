from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=16)
    description = models.CharField(max_length=256)

class Post(models.Model):
    title = models.CharField(max_length=256)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/', blank=True)
    content = models.CharField(max_length=2048)
    created_at = models.TimeField(auto_now_add=True)
    modificated_at = models.TimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)



