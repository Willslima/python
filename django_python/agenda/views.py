from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

# from agenda.models import eventos

# Create your views here.
def index(request):
    return HttpResponse('Olá mundo')

def exibir_evento(request):
    evento = {
        'nome':'Teste',
        'categoria':'categoria A',
        'local':'Rio de Janeiro'
    }

    return render(request=request, context={'evento':evento}, template_name='agenda/exibir_evento.html')