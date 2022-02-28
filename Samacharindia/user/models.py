from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email=models.CharField(max_length=120)
    message=models.CharField(max_length=500)

    # To show only one field of table in admin page
    def __str__(self):
        return self.name

class category(models.Model):
    CName=models.CharField(max_length=120)
    CPic=models.ImageField(upload_to='static/category/',default="")
    CDate=models.DateField()

    def __str__(self):
        return self.CName



class news(models.Model):
    ncity=models.CharField(max_length=500)
    nhead=models.CharField(max_length=1000)
    # news class is use category class as foriegn key
    ncategory=models.ForeignKey(category,on_delete=models.CASCADE)
    nsubject=models.CharField(max_length=200)
    ndes=HTMLField()
    ndate=models.DateField()
    npic=models.ImageField(upload_to='static/news/',default="")

class videonews(models.Model):
    vlink=models.CharField(max_length=600)
    vtitle=models.TextField(max_length=1000)
    vnews=models.TextField(max_length=5000)
    vcity=models.CharField(max_length=500)
    vcategory=models.ForeignKey(category,on_delete=models.CASCADE)
    vdate=models.DateField()

class notification(models.Model):
    ndes=models.TextField(max_length=1000)
    ndate=models.DateField()

class slider(models.Model):
    spic=models.ImageField(upload_to='static/slider',default="")
    stitle=models.CharField(max_length=500)
    sdes=models.TextField(max_length=2000)
    sdate=models.DateField()

