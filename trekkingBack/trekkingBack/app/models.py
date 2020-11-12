"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Tipo_treeking(models.Model):
    Id_tipo = models.AutoField(primary_key=True)
    Name_tipo = models.CharField(max_length = 100)     
    Description_tipo = models.CharField(max_length = 5000)  
    Active_tipo = models.BooleanField()

    def __str__(self):
        return self.Name_tipo


class Treeking(models.Model):
    Id_treeking = models.AutoField(primary_key=True)
    Name_treeking = models.CharField(max_length = 100)
    Description_treekingr = models.CharField(max_length = 5000)      
    Id_tipo = models.ForeignKey(Tipo_treeking,  related_name='treeking', on_delete=models.CASCADE)
    Activo_treeking = models.BooleanField()

    def __str__(self):
        return self.Name_treeking
