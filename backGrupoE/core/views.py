from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def cotizarreparacion(request):
    return render(request, "core/cotizarreparacion.html")


def nosotros(request):
    return render(request, "core/nosotros.html")