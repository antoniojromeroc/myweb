from abc import abstractclassmethod
from distutils.command.upload import upload
from pyexpat import model
from django.conf import settings
from django.db import models
from sqlalchemy import true
from ckeditor.fields import RichTextField
from django.conf.urls.static import static

pathMyblogImg = settings.PATH_MYBLOG_IMAGES

# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(primary_key=true)
    estado = models.BooleanField(default = True)
    created_at = models.DateField(auto_now = False, auto_now_add = True)
    modified_at = models.DateField(auto_now = True, auto_now_add = False)
    eliminated_at = models.DateField(auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

class Categoria(ModelBase):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    imagen_referencial = models.ImageField(upload_to = pathMyblogImg +'categorias/')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        # db_table = 'Categoria'
        # ordering = ['apellido_paterno', '-apellido_materno']

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.descripcion)

class Subcategoria(ModelBase):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    imagen_referencial = models.ImageField(upload_to = pathMyblogImg +'subcategorias/')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.categoria)

class Author(ModelBase):
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    nombres = models.CharField(max_length=50, verbose_name="Nombres")
    email = models.EmailField(max_length = 200)
    descripcion = models.TextField()
    web = models.URLField(null = True, blank = True)
    Facebook = models.URLField(null = True, blank = True)
    Twitter = models.URLField(null = True, blank = True)
    instagram = models.URLField(null = True, blank = True)
    photo = models.ImageField(upload_to = pathMyblogImg +'autores/')
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def nombre_completo(self):
        return "{}, {}". format(self.apellidos, self.nombres)

    def __str__(self):
        return self.nombre_completo()

class Articulos(ModelBase):
    titulo = models.CharField(max_length=50, unique = True)
    slug = models.CharField(max_length=50, unique = True)
    descripcion = models.CharField(max_length=150)
    ruta = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, null=True, blank=True, on_delete=models.CASCADE)
    autor = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    imagen_referencial = models.ImageField(upload_to = pathMyblogImg +'articulos/')
    publicado = models.BooleanField(default = False)
    fecha_publicacion = models.DateField()
    contenido = RichTextField()

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'    

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.subcategoria)


#     class Meta:
#         verbose_name = 'Docente'
#         verbose_name_plural = 'Docentes'
#         db_table = 'Docente'
#         ordering = ['apellido_paterno', '-apellido_materno']
