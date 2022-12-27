from .models import Cart


def get_or_create_cart(request):
     #Vamos a crear un session
    #request.session['cart_id']='123'  #Dic

    #consulto session
    #valor=request.session.get('cart_id')
    #print(valor)

    #Eliminar una session
    #request.session['cart_id']=None

    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')   #None si la llave no exista
    cart = Cart.objects.filter(cart_id=cart_id).first() #[] -> None

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:    
        cart.user=user
        cart.save()

    request.session['cart_id']=cart.cart_id

    return cart









