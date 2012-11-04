from django.contrib import admin
from django.db import models
from django import forms

class Imagem(models.Model):
    descricao = models.CharField(max_length=20)
    imagem = models.ImageField("imagem", upload_to="images/", blank=True, null=True)

    def __unicode__(self):
        return self.descricao

class Produto(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=20)
    imagem = models.ForeignKey(Imagem)

    def __unicode__(self):
        return self.nome

# Create your models here.
class Destaque(models.Model):
    titulo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100, blank=True,null=True)
    imagem = models.ForeignKey(Imagem)

    def __unicode__(self):
        return self.titulo

# Import our custom widget and our model from where they're defined

class DestaqueModelForm( forms.ModelForm ):
    descricao = forms.CharField( widget=forms.Textarea,required=False)

    class Meta:
        model = Destaque



