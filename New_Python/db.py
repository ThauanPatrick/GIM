from django.db import models

class imagens(models.Model):
    banda = models.IntegerField()
    superior_x = models.IntegerField()
    superior_y = models.IntegerField()
    inferior_x = models.IntegerField()
    inferior_y = models.IntegerField()
    tipo_banda = models.CharField(max_length=10)
    tamanho_pixel = models.IntegerField()
    projecao = models.CharField(max_length=255)
    driver = models.CharField(max_length=20)
    nuvens = models.IntegerField()
    satelite = driver = models.CharField(max_length=20)
    sensor = driver = models.CharField(max_length=20)
    data = models.DateField()
    orbita = models.IntegerField()
    caminho = models.CharField(max_length=255)
    nome = models.CharField(max_length=100)
    xml = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


