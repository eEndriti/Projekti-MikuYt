from django.db import models


# Create your models here.

class categorite(models.Model):
    name = models.CharField(max_length=100)


class animacionet(models.Model):
    id = models.AutoField(primary_key=True)
    categoryId = models.ForeignKey(categorite, on_delete=models.CASCADE)
    emriianimacionit = models.CharField(max_length=100)
    gifi = models.ImageField(upload_to='gallery')
