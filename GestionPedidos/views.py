from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


from .forms import ContactForm

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

def contact(request):
    
    myForm = ContactForm()
    
    if request.method == "POST":
        myForm = ContactForm(request.POST)

        if myForm.is_valid() :
            infoForm = myForm.cleaned_data
            print(infoForm)
            send_mail(infoForm['name'],infoForm["message"], infoForm.get("email",""),["lordchief21@gmail.com"],)
        else:
            myForm = ContactForm()
    
    return render(request, "formulario_contacto.html", {"form": myForm})





    return render(request, "contacto.html")