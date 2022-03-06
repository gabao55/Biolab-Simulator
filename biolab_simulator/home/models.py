from tkinter import CASCADE
from unicodedata import name
from django.db import models


class Home(models.Model):
    id = models.BigIntegerField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name='Home name', max_length=50)
    intro = models.TextField(verbose_name='Introduction')

    def __str__(self) -> str:
        return self.name + ' Page'


class Image(models.Model):
    home_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    id = models.BigIntegerField(verbose_name='id', primary_key=True)
    label = models.CharField(verbose_name='Label', max_length=200)
    image = models.ImageField(verbose_name='Image')

    def __str__(self) -> str:
        return 'Image ' + str(self.id) + ' - ' + str(self.label)