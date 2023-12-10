from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20, verbose_name = 'titulo')
    image = models.ImageField(verbose_name = 'imagen', upload_to="projects")
    description = models.CharField(max_length=20, verbose_name = 'precio')
    create = models.DateTimeField(auto_now_add=True, verbose_name = 'fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name = 'fecha de modificacion')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-create']