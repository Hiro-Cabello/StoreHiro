from django.contrib import admin

# Register your models here.

from .models import Cart 

#admin.site.register(Cart)

class CartAdmin(admin.ModelAdmin):
    list_display=('cart_id','user','created_at')


admin.site.register(Cart,CartAdmin)

