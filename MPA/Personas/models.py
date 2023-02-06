from django.db import models

# Create your models here.
class Universo(models.Model):
    id = models.CharField(primary_key=True,max_length=3)
    image_url = models.CharField(max_length=99999)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.id)


class Personaje(models.Model):
    codigo = models.CharField(primary_key=True,max_length=4)
    image_url = models.CharField(max_length=99999)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.PositiveSmallIntegerField()
    nacionalidad = models.CharField(max_length=15)
    raza = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=70)
    universo=models.ForeignKey(Universo, on_delete=models.CASCADE,null=False)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.codigo)