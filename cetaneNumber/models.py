from django.db import models

class PredictiveModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50 ,verbose_name="Model's name")
    brief_description = models.CharField(max_length=500, verbose_name="Brief description for home page")
    description = models.TextField(verbose_name="Model's description")

    def __str__(self) -> str:
        return self.name


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