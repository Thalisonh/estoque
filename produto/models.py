from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome_categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, null = True, blank = True)
    nome_item = models.CharField(max_length = 100, null = True, blank = True)
    quantidade_total = models.IntegerField(default = 0, null = True, blank = True)
    quantidade_emitida = models.IntegerField(default = 0, null = True, blank = True)
    quantidade_recebida = models.IntegerField(default = 0, null = True, blank = True)
    preco_unitario = models.IntegerField(default = 0, null = True, blank = True)

    def __str__(self):
        return self.nome_item

class Venda(models.Model):
    item = models.ForeignKey(Produto, on_delete = models.CASCADE)
    quantidade = models.IntegerField(default = 0, null = True, blank = True)
    quandidade_recebida = models.IntegerField(default = 0, null = True, blank = True)
    cliente = models.CharField(max_length = 100, null = True, blank = True)
    preco_unitario = models.IntegerField(default = 0, null = True, blank = True) 

    def __str__(self):
        return self.item.nome_item