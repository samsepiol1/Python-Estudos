from django.shortcuts import render,HttpResponse
from . import script_cotacao

# Create your views here.

def pagina_inicial(request):
    cotacao_bitcoin = script_cotacao.valor_bitcoin
    return render(request,'C:/Users/Deus.DEUS.002/PycharmProjects/untitled/templates/home.html',{"moeda":cotacao_bitcoin})
