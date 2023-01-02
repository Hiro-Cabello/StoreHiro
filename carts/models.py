import uuid
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import decimal

#Lista de todas las señales que envia Django.
from django.db.models.signals import pre_save ,post_save

from django.db.models.signals import m2m_changed



# Create your models here.
class Cart(models.Model):

    cart_id = models.CharField(max_length=100,null=False,blank=False,unique=True)

    #UNO A MUCHOS
    user = models.ForeignKey(User , null=True ,blank=True,  on_delete=models.CASCADE)

    #MUCHOS A MUCHOS
    #Recordar que cuando se va generar primero se hace un migrate del cart y cartproduct y luego trabajamos o descomentamos la relacion que hay entre ellos
    products =  models.ManyToManyField(Product,through='CartProduct')
    subtotal = models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    total = models.DecimalField(default=0.0,max_digits=8 , decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    FEE = 0.05 #Comision

    def __str__(self):
        return self.cart_id

    def update_totals(self):
        self.update_subtotal()
        self.update_total()
    
    def update_subtotal(self):
        #self.subtotal=sum([product.price for product in self.products.all()])
        self.subtotal = sum([
            cp.quantity*cp.product.price for cp in self.products_related()
        ])
        self.save()

    #Suma el total + una comision
    def update_total(self):
        self.total=self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()

    def products_related(self):

        #Aqui vamos a colocar la relacion con otro producto
        #Con esta linea vamos obtener todos los productos cartproduct
        #Y los objetos productos en una sola consulta
        #Recordar qe select_related nos evita el uso de all()
        #Ahora obtenermos la misma info con una sola consulta los cartproduct y product
        return self.cartproduct_set.select_related('product')

#Esta clase va heredar de models.Manager
#Cuando creamos un objeto lo que vamos a hacer es asignarle una cantidad 
class CartProductManager(models.Manager):

    #Esta clase va obtener los metodos que uno desea extender
    def create_or_update_quantity(self,cart,product,quantity=1):
        #si el objeto no existe en la base de datos pues procede a crearlo
        object , created = self.get_or_create(cart=cart,product=product)

        if not created:
            #object.quantity += int(quantity)
            quantity = object.quantity + int(quantity)

        #Con esto siempre que se cree o se actualize siempre se va a modificar la cantidad 
        object.update_quantity(quantity)
  
        return object


class CartProduct(models.Model):
    #vamos a definir primero la relacion de un carrito y un producto
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    product=models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects=CartProductManager()

    def update_quantity(self,quantity=1):
        self.quantity = quantity
        self.save()


def set_cart_id(sender,instance,*args,**kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

#
def update_totals(sender,instance,action,*args,**kwargs):
    #vamos a registrar las acciones que nos interesan en cualquiera de esos casos vamos a actualizar los casoss
    if  action == 'post_add' or action=='post_remove' or action=='post_clear':
        instance.update_totals()

def post_save_update_totals(sender,instance,*args,**kwargs):
    instance.cart.update_totals()


#Esto se envía al principio del metodo save() de un modelo.
pre_save.connect(set_cart_id , sender = Cart)
post_save.connect(post_save_update_totals , sender=CartProduct)
#Se envia cuando se cambia un ManyToManyField en un modelo instancia.
#Estrictamente hablando, esta no es una señal de modelo, ya que es enviada
#por ManToManyField , pero dato que complemente el pre_save / post_save y pre_delete /post_delete
#cuando se trata de rastrear cambios en los modelos.
m2m_changed.connect(update_totals , sender=Cart.products.through)

    

