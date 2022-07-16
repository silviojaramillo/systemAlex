from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Project(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Id")
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(null=True,verbose_name="Descripción")
    image = models.ImageField(upload_to='projects', null=True, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]
    def __str__(self):
        return self.title