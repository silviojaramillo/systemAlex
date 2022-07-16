from distutils.command import upload
from tabnanny import verbose
from django.db import models

# Create your models here.

class AboutMe(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nombres')
    last_name = models.CharField(max_length=100, verbose_name='Apellidos')
    biography = models.TextField(null = True, verbose_name='Biografía')
    image = models.ImageField(upload_to = 'about', null = True, verbose_name='Imagen')
    class Meta:
        verbose_name = 'Biografía'
        verbose_name_plural = 'Biografías'
    def __str__(self):
        return self.name