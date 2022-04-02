from atexit import register
from django.template import Library

register = Library()

@register.filter
def get_name(model, name):
    return model.get(name=name)