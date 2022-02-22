from django.contrib import admin
from .models import Articulos, Author, Categoria, Subcategoria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Author)
admin.site.register(Articulos)