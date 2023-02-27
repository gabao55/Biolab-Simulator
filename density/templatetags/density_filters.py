from django.template import Library

register = Library()

@register.filter
def get_compounds(compounds, esther_type):
    return compounds.filter(esther_type=esther_type).order_by(("name"))