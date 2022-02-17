from operator import mod
from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
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


#TODO: Repair django summernote
class PredictiveModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ['id', 'name']
    inlines = [
        EquationsInline,
        GraphsInline,
        CompoundsInline,
    ]


class CompoundAdmin(admin.ModelAdmin):
    list_display = ['getModel', 'name']
    inlines = [
        ParametersInline
    ]


admin.site.register(models.PredictiveModel, PredictiveModelAdmin)
admin.site.register(models.Compound, CompoundAdmin)
admin.site.register(models.Equation)
admin.site.register(models.Graph)
admin.site.register(models.Parameter)