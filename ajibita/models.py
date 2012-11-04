from django.db import models
from django import forms


class Seccoes(models.Model):
    nome = models.CharField(max_length=20)
    texto = models.TextField(max_length=2000)

    def __unicode__(self):
        return self.nome


class SeccoesModelForm( forms.ModelForm ):
    texto = forms.CharField( widget=forms.Textarea,required=False)
    class Meta:
        model = Seccoes

