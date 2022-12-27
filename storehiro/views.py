#Cuendo trabajo con templates
from xmlrpc.client import boolean
from django.shortcuts import redirect, render

from django.http import HttpResponse 


from django.contrib.auth import authenticate


#Encargada de la session
from django.contrib.auth import login , logout


#Para enviar mensajes del servidor al cliente
from django.contrib import messages

from storehiro.forms import RegisterForm


#Vamos a inportar el registro
from .forms import RegisterForm

from django.contrib.auth.models import User #Con esta clase vamos a de alta nuevos usuarios

#def index(request):
#    return HttpResponse('Hola Mundo')ç



#Importando el modelo
from products.models import Product


#from users.models import User


#Notas a partir de el contexto yo puedo pasar valores de nuestra lista a nuestro template
def index(request):

    products = Product.objects.all().order_by('-id')

    return render(request,'index.html',{
        'message':'Store Hiro',
        'title':'Productos',
        'productos':products,
        #'productos':[
        #    {'title':'Playera','price':5,'stock':True},
        #    {'title':'Camisa','price':7,'stock':True},
        #    {'title':'Mochila','price':20,'stock':False}
        #]
    })


def login_view(request):

    #if request.user.is_authenticated:
    #    return redirect('index')

    if request.method =='POST':
        #Con esto recupero el valor
        #que estoy ingresando en el primer formulario
        username= request.POST.get('username')
        password= request.POST.get('password')

        print(username)
        print(password)

        #si en caso no lo encuentra pasara none
        user= authenticate(username=username,password=password)
        if user:
            login(request,user)
            print("Usuario autenticado")
            messages.success(request,'Bienvenido {} '.format(user.username))

            return redirect('index')#le pongo el name del home
        else:
            print("Usuario no autenticado")
            messages.error(request,'Usuario o contraseña no validos')
        
    return render(request,'users/login.html',{ })


def logout_view(request):
    logout(request)
    messages.success(request,'Sesion cerrada exitosamente')
    return redirect('login')


def register(request):

    #if request.user.is_authenticated:
    #    return redirect('index')
    form=RegisterForm(request.POST or None) #Con esto le indico complete el formulario con los datos pasaddos o sino hay que sea vacio
    #crea el formulario con datos  sin datos

    if request.method=='POST' and form.is_valid() :

        user = form.save()

        #username= form.cleaned_data.get('username')
        #email=form.cleaned_data.get('email')
        #password=form.cleaned_data.get('password')

        #user = User.objects.create_user(username,email,password)

        if user:
            login(request,user)
            messages.success(request , 'Usuario creado exitosamente')
            return redirect('index')


    return render(request,'users/register.html',{ 
        'form':form     
    })






















