from django.shortcuts import render_to_response
from shop.models import  Promocao, Produto

def home(request):
    promocoes = Promocao.objects.all()
    produtos = Produto.objects.all()
    return render_to_response('ajibita/index.htm',{'promocoes' : promocoes, 'produtos':produtos})

def test(request):
    return render_to_response('ajibita/teste.htm')