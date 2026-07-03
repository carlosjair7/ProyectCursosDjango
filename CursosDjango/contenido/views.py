from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def principal(request):
    return render(request,"contenido/principal.html")

def prueba(request):
    
    return render(request,"contenido/nombre.html")

def contacto(request):
    return render(request,"contenido/contacto.html")
    

def formulario(request):
    return render(request,"contenido/formulario.html")

def ejemplo(request):
    return render(request,"contenido/ejemplo.html")
    
