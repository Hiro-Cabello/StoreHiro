from django.db import models

# Create your models here.
#Representacion de una tabla en la base de datos

#Importar el slug de django
#Slug es una etiqueta corta para algo, que contiene solo letras, numeros,
#   guiones bajos o guiones.
#Slugify Convierte una cadena en un slug de URL.
from django.utils.text import slugify


#signal
#Una lista de todas las señales que envia DJANGO.
#pre_save
#Se envia al comienzo del save() metodo de un modelo.
from django.db.models.signals import pre_save

#Es una biblioteca de Python que ayuda a gnerar
#objetos de aleatorios de 128 bits como identificadores.
import uuid

class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2,default=0.0)

    slug = models.SlugField(null=False,blank=False , unique=True)

    #Imagen
    #upload_to='' sirve para almacenar la ruta
    image = models.ImageField(upload_to='products/',null=False , blank=False)

    created_at=models.DateTimeField(auto_now_add=True)#El valor se toma de
    #forma automatica
    #Slug automaticos
    #def save(self , *args , **kwargs):
    #    self.slug = slugify(self.title) 
    #    super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

#la instancia va ser nuestro producto
def set_slug(sender,instance , *args,**kwargs): #callbak
    #La documentacion indica que el callback debe de recibir 5 argumentos

    #si mi objeto posee un titulo o no posee un slug
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        

        #Con esto yo me aseguro de generar un slug unico de la base de datos
        #
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title,str(uuid.uuid4())[:8] )
            )


        #Asignarle al objeto
        instance.slug = slug

#Con esto le indicamos a django que antes que un objeto se almacene
#se va ejecutar el pre_save
pre_save.connect(set_slug,sender=Product)



