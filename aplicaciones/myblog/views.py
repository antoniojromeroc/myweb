from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    # messages.success(request, 'Mensaje de prueba para ver dismisibilidad')
    return render(request, "home.html") #, {"cursos": cursos})