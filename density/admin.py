from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


class CompoundsInline(admin.TabularInline):
    model = models.Compound
    extra = 1


class ParametersInline(admin.TabularInline):
    model = models.Parameter
    extra = 1


class PredictiveModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ['name']
    inlines = [CompoundsInline]


class CompoundAdmin(admin.ModelAdmin):
    list_display = ['getModel', '__str__']
    inlines = [
        ParametersInline
    ]
    ordering = ('esther_type', 'name')


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['getCompound', 'name', 'value']

admin.site.register(models.PredictiveModel, PredictiveModelAdmin)
admin.site.register(models.Compound, CompoundAdmin)
admin.site.register(models.Parameter, ParameterAdmin)