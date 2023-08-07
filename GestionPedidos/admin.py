from django.contrib import admin

from GestionPedidos.models import Clientes,Articulos,Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre","direccion","tfno")
    search_fields = ("nombre", "tfno")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("sección",)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero","fecha","entregado")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"


# Register your models here.
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)