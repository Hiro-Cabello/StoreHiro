from django import template

register = template.Library()

#Para que una funcion se convierta en filter bastaria con decorarla
@register.filter()
def price_format(value):
    return '${0:.2f}'.format(value)




