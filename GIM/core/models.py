from django.db import models

class imagens(models.Model):

    banda = models.IntegerField(null=True, blank=True)
    superior_x = models.IntegerField(null=True, blank=True)
    superior_y = models.IntegerField(null=True, blank=True)
    inferior_x = models.IntegerField(null=True, blank=True)
    inferior_y = models.IntegerField(null=True, blank=True)
    tipo_banda = models.CharField(max_length=10, null=True, blank=True)
    tamanho_pixel = models.IntegerField(null=True, blank=True)
    projecao = models.TextField(null=True, blank=True)
    tipo_imagem = models.CharField(max_length=20, null=True, blank=True)
    nuvens = models.IntegerField(null=True, blank=True)
    satelite = models.CharField(max_length=20, null=True, blank=True)
    sensor = models.CharField(max_length=20, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    orbita = models.IntegerField(null=True, blank=True)
    caminho = models.TextField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    xml = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome



