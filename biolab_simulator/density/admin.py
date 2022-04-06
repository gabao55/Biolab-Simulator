from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


class EquationsInline(admin.TabularInline):
    list_display = ['getModel', 'number']
    model = models.Equation
    extra = 1


class GraphsInline(admin.TabularInline):
    model = models.Graph
    extra = 1


class CompoundsInline(admin.TabularInline):
    model = models.Compound
    extra = 1


class ParametersInline(admin.TabularInline):
    model = models.Parameter
    extra = 1


class PredictiveModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ['name']
    inlines = [
        EquationsInline,
        GraphsInline,
        CompoundsInline,
    ]


class CompoundAdmin(admin.ModelAdmin):
    list_display = ['getModel', '__str__']
    inlines = [
        ParametersInline
    ]
    ordering = ('esther_type', 'name')


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['getCompound', 'name', 'value']


class GraphAdmin(admin.ModelAdmin):
    list_display = ['getModel', 'label']

admin.site.register(models.PredictiveModel, PredictiveModelAdmin)
admin.site.register(models.Compound, CompoundAdmin)
admin.site.register(models.Equation)
admin.site.register(models.Graph, GraphAdmin)
admin.site.register(models.Parameter, ParameterAdmin)