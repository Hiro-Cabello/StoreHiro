from django.shortcuts import render
from .models import Cart
from .utils import get_or_create_cart
from products.models import Product
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import CartProduct


# Create your views here.
#En las vistas tengo que enviar el argumento o dato que voy a pintar en el template
def cart(request):
    cart = get_or_create_cart(request)
    return render(request , 'carts/cart.html' ,{
        'cart':cart
    } )


def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    #El formulario nos envia la cantidad cuyo input es quantity
    #storehiro\carts\templates\carts\snippets\add.html
    #Con esto recupero del formulario
    #                                       es 1 si es que la llave no existe
    quantity = request.POST.get('quantity',1)

    #                           este parametro no es más que un diccionario
    #Con esto podemos agregar la cantidad de un producto a un carrito de compras
    #cart.products.add(product , through_defaults={'quantity':quantity})

    #
    cart_product = CartProduct.objects.create_or_update_quantity(cart=cart
                                                ,product=product
                                                ,quantity=quantity)

    return render(request , 'carts/add.html',{
        'quantity':quantity,
        'cart_product':cart_product,
        'product':product
    })


def remove(request):
    #La excepcion manda un codigo de 500 al cliente indicando que hubo un error en el servidor
    #pagenotfound envia un codigo 404 inidicandole al cliente que hay un recurso no encontrado   

    #Nos permitira obtener un objeto a partir de una excepcion
    #get_object_or_404

    #vamos a obtener el carrito de compras
    cart = get_or_create_cart(request)

    #vamos a obtener el producto bajo la llave product_id
    #product = Product.objects.get(pk=request.POST.get('product_id'))
    product =get_object_or_404(Product ,pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')    