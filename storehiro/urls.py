from django.contrib import admin
from django.urls import path
from products.views import ProductListView
from . import views
from products.views import ProductListView
from django.urls import include

#Para usar las constantes creadas con imagenes
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.index , name='index'),
    #Con este metodo le indicamos a django que vamos a usar la clase como una vista......
    path('',ProductListView.as_view() , name='index'),
    path('usuarios/logout',views.logout_view , name='logout'),
    path('usuarios/login',views.login_view,name='login'),
    path('usuarios/registro',views.register , name='register'),

    path('productos/' , include('products.urls')),

    path('carrito/',include('carts.urls')),
]
#Vamos a condicionar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




