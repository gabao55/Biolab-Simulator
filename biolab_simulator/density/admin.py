from operator import mod
from django.contrib import admin
from . import models


# Register your models here.
class EquationsInline(admin.TabularInline):
    model = models.Equations
    extra = 1


class GraphsInline(admin.TabularInline):
    model = models.Graphs
    extra = 1


class CompoundsInline(admin.TabularInline):
    model = models.Compound
    extra = 1


class ParametersInline(admin.TabularInline):
    model = models.Parameters
    extra = 1


class AbsoluteParameterInline(admin.TabularInline):
    model = models.AbsoluteParameter
    extra = 1


class PredictiveModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [
        EquationsInline,
        GraphsInline,
        CompoundsInline,
        AbsoluteParameterInline
    ]


class CompoundAdmin(admin.ModelAdmin):
    list_display = ['getModel', 'name']
    inlines = [
        ParametersInline
    ]


admin.site.register(models.PredictiveModel, PredictiveModelAdmin)
admin.site.register(models.Compound, CompoundAdmin)
admin.site.register(models.Equations)
admin.site.register(models.Graphs)
admin.site.register(models.AbsoluteParameter)
admin.site.register(models.Parameters)