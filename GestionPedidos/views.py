from django.http import HttpResponse
from django.shortcuts import render
from more_itertools import product_index

from .models import Articulos

# Create your views here.

def upload_template(request):
    return render(request,"index.html")

def search_product(request):
    if request.GET["product"]:
        product = request.GET["product"]
        articles = Articulos.objects.filter(nombre__icontains = product)
        return render(request, "resultado_busqueda.html", {"articles" : articles, "query": product})
    else:
        message = 'No colocaste ningún producto'
    
    return HttpResponse(message)