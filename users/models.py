from django.db import models

# Create your models here.
#Proxy model es un modelo que hereda de otro, y su diferencia este no genera una tabla en la base de datos

from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser


#class User(AbstractUser):

#    def get_full_name(self):
#        return '{} {}'.format(self.first_name , self.last_name)


class Customer(User):
    class Meta:       #Esto hara que el modelo no generé nuevas tablas
        proxy = True  #Defino el atributo proxy como verdadero.

    
    def get_products(self):
        return []

class Profile(models.Model):
    #Relacion uno a uno con user por parte de Profile
    #                                  #Esto indica que cuando se elimine un usuario se elimine su profile
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio  = models.TextField()



