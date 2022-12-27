from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from django.views.generic.detail import DetailView

#Con esto vamos a poder hacer consultas con diversos filtros
from django.db.models import Q

from products.models import Product

class ProductListView(ListView):#Cuando se hereda de listview pues se debe de definir
    #template_name y  queryset
     #template_name---> Nombre del template a usar
     #queryset ---> Es la consulta para encontrar el listado de objetos
    template_name='index.html'
    #el estado de objetos
    queryset =  Product.objects.all().order_by('id')

    #Pasamos el contexto de la clase al template
    def get_context_data(self , **kwargs):
        context=super().get_context_data(**kwargs)#Con esto obtengo el contexto de la clase padre
        context['message']='Listado de productos'
        context['productos'] = context['object_list']
        #productos<-----object_list
        #Dentro de este contecto se le manda los productos
        #Se imprime para poder verlos y analizarlos
        print(context)

        return context


  

#Para visualizar el detalle vamos a heredar
#de la clase detailview
class ProductDetailView(DetailView):#Por defecto la busqueda es por pk
    #El valor de la identificacion lo tomará de la url por 
    #eso es necesario tomarlo
    #Temenos que especificar el Model y el template
    model = Product 
    template_name = 'products/product.html'

#De esta forma como se le pasa el contexto a la clase product.html
    def get_context_data(self , **kwargs):
        context=super().get_context_data(**kwargs)
        #product
        print(context)

        return context



class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        #---No busca por el titulo de la categoria....26/07/2022
        # and ,
        # or  |
        filters =Q(title__startswith=self.query()) | Q(title__icontains=self.query()) #| Q(category__title__icontains=self.query() ) 
        #select * from products where title like %valor%
        #La i indica que no es sensible a mayusculas ni minusculas
        #return Product.objects.filter(title__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self , **kwargs):
        context=super().get_context_data(**kwargs)
        #product
        context['query'] = self.query()
        context['count']=context['product_list'].count()

        return context


