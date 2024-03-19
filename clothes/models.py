from django.contrib.postgres.fields import ArrayField
from django.db import models

from dataset.models import Dataset

def upload_to(instance, filename):
    return 'clothes/images/{filename}'.format(filename=filename)

class Clothes(models.Model) :
    colour_model = models.CharField(max_length=120)
    file_extension = models.CharField(max_length=120, null=True, blank=True)
    width = models.BigIntegerField()
    height = models.BigIntegerField()
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) :
        return self.name


class Segmentation(models.Model) :
    part = models.CharField(max_length=120)
    size = models.BigIntegerField()
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, null=True, blank=True)
    segmantation_colour = ArrayField(models.JSONField())

    def __str__(self) :
        return f"{self.clothes} - {self.part} - segmentation"