from django.contrib import admin

# Register your models here.

from .models import Product

#Con esto voy a modificar lo que se muestra en admin
#Esta clase ProductAdmin es la que va nos ayudara a modificar
#lo que se muestra en el admin
class ProductAdmin(admin.ModelAdmin):
    fields=('title','description','price','image')
    list_display = ('__str__','slug')

admin.site.register(Product,ProductAdmin)

