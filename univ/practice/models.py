from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Data(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.FileField(upload_to='tmp/')

class Img(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    xlim_l = models.IntegerField()
    xlim_r = models.IntegerField()
    ylim_l = models.IntegerField()
    ylim_r = models.IntegerField()
    k = models.IntegerField(null=True)
    img = models.ImageField(upload_to='img/')
