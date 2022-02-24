from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


class ImageInline(admin.TabularInline):
    list_diplay = ['__str__', 'image']
    model = models.Image
    extra = 1


class HomeAdmin(SummernoteModelAdmin):
    summernote_fields = ('intro', )
    list_display = ['__str__']


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'image']

admin.site.register(models.Home, HomeAdmin)