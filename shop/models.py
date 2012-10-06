from django.db import models


class Produto(models.Model):
    nome=models.CharField(max_length=20)
    descricao=models.CharField(max_length=20)
    imagem = models.ImageField("imagem", upload_to="images/", blank=True, null=True)

    def __unicode__(self):
        return self.nome

# Create your models here.
class Promocao(models.Model):
    titulo=models.CharField(max_length=20)
    descricao=models.CharField(max_length=100)
    produto=models.ForeignKey(Produto)

    def __unicode__(self):
        return self.titulo