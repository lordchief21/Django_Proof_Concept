from django.contrib import admin

from GestionPedidos.models import Clientes,Articulos,Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre","direccion","tfno")
    search_fields = ("nombre", "tfno")


# Register your models here.
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos)
admin.site.register(Pedidos)