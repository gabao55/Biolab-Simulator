from tkinter import CASCADE
from django.db import models

# Create your models here.
class PredictiveModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50 ,verbose_name="Model's name")
    description = models.TextField(verbose_name="Model's description")

    def __str__(self) -> str:
        return self.name


class Equation(models.Model):
    model_id = models.ForeignKey(PredictiveModel, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="Equation's number", blank=True)
    equation = models.ImageField(verbose_name="Equation's image")

    def __str__(self) -> str:
        return str(self.model_id.name) + "'s " + "equation " + str(self.number)

    def getModel(self) -> str:
        return self.model_id.name


class Graph(models.Model):
    model_id = models.ForeignKey(PredictiveModel, on_delete=models.CASCADE)
    label = models.CharField(max_length=100 ,verbose_name="Graph's label", blank=True)
    image = models.ImageField(verbose_name="Graph's image")

    def __str__(self) -> str:
        return self.label

    def getModel(self) -> str:
        return self.model_id.name


class Compound(models.Model):
    model_id = models.ForeignKey(PredictiveModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50 ,verbose_name="Compound's representation", blank=True)
    esther_type = models.CharField(max_length=50, verbose_name="Esther type", blank=True)

    def __str__(self) -> str:
        return self.name

    def getModel(self) -> str:
        return self.model_id.name

class Parameter(models.Model):
    compound_id = models.ForeignKey(Compound, on_delete=models.CASCADE)
    name = models.CharField(max_length=50 ,verbose_name="Parameter's name")
    value = models.FloatField(verbose_name="Parameter's value")

    def __str__(self) -> str:
        return self.name

    def getCompound(self) -> str:
        return self.compound_id.name