from django.db import models

class imagens(models.Model):

    banda = models.FloatField(null=True, blank=True)
    superior_x = models.FloatField(null=True, blank=True)
    superior_y = models.FloatField(null=True, blank=True)
    inferior_x = models.FloatField(null=True, blank=True)
    inferior_y = models.FloatField(null=True, blank=True)
    tipo_banda = models.CharField(max_length=40, null=True, blank=True)
    tamanho_pixel = models.FloatField(null=True, blank=True)
    projecao = models.TextField(null=True, blank=True)
    tipo_imagem = models.CharField(max_length=40, null=True, blank=True)
    nuvens = models.FloatField(null=True, blank=True)
    satelite = models.CharField(max_length=40, null=True, blank=True)
    sensor = models.CharField(max_length=40, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    orbita = models.FloatField(null=True, blank=True)
    caminho = models.TextField(null=True, blank=True)
    nome = models.CharField(max_length=255)
    xml = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome