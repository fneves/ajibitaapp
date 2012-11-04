from django.shortcuts import render_to_response
from ajibita.models import Seccoes
from shop.models import  Destaque, Produto

def home(request):
    destaques = Destaque.objects.all()
    produtos = Produto.objects.all()
    textos = {}
    for seccao in Seccoes.objects.all():
        textos[seccao.nome] = seccao.texto

    return render_to_response('ajibita/index.htm',{'destaques' : destaques,
                                                   'produtos':produtos,
                                                   'textos' : textos})

#def test(request):
#    return render_to_response('ajibita/teste.htm')