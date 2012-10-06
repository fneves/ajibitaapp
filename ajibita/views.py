from django.shortcuts import render_to_response

def home(request):
    return render_to_response('ajibita/index.htm')

def test(request):
    return render_to_response('ajibita/teste.htm')