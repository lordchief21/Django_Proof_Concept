from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def upload_template(request):
    return render(request,"index.html")

def search_product(request):
    message = 'Producto econtrado: %r'%request.GET["product"]
    return HttpResponse(message)