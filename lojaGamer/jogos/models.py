from django.db import models


class Categoria(models.Model):

    categoria = models.CharField(max_length=45)

    def __str__(self):
        return self.categoria


class Jogo(models.Model):
    
    nome = models.CharField(max_length=45)
    categoria = models.ForeignKey('Categoria', null = True, on_delete=models.CASCADE)
    distribuidora = models.CharField(max_length=45)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome
    
    def disponivel(self):
        return bool(self.estoque)

 

