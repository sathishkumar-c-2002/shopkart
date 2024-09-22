from django.db import models
import datetime
import os


# Create your models here.

def getFileName(request,filename):
    now_time = datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    new_file_name = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_file_name)

class Category(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    vendor = models.ImageField(upload_to=getFileName,null=True,blank=True)
    prodcut_image = models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending  = models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


        