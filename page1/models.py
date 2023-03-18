from django.db import models

# Create your models here.

class Prodcuts(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.CharField(max_length=500)


    def __str__(self) :
        return self.name