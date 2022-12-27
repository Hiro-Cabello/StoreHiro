from django.urls import path

from . import views

# Con esto se indica que todas estas rutas le pertenecen unicamente a la aplicacion de producto
# y con esto vamos a evitar el conflicto de rutas
app_name = 'products'

urlpatterns=[

    #path('<pk>' , views.ProductDetailView.as_view(),name='product') #id-->llave primaria
    #Ahora vamos buscar <slug por el campo slug que es del tipo slug
    path('search' , views.ProductSearchListView.as_view(),name='search'),
    path('<slug:slug>' , views.ProductDetailView.as_view(),name='product') ,

]


