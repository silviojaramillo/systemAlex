from distutils.command.upload import upload
from django.db import models

class Project(models.Model):
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,verbose_name="Descripción")
    image = models.ImageField(upload_to='images/', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
