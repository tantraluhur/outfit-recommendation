from django.db import models

class Dataset(models.Model) :
    name = models.CharField(max_length=120)
    source_type = models.CharField(max_length=120)
    generation = models.CharField(max_length=120)
    season = models.CharField(max_length=120)

    def __str__(self) :
        return self.name
