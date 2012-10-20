from django.shortcuts import render_to_response
from shop.models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render_to_response('ajibita/index.htm',{"produtos" : produtos})

def test(request):
    return render_to_response('ajibita/teste.htm')