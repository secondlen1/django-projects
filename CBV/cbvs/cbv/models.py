from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=124)
    content =  models.CharField(max_length=512)
    created = models.DateField(auto_now=True)
    modified = models.DateField(auto_now_add=True)
    
