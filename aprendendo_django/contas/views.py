from django.shortcuts import render,HttpResponse


# Create your views here.
def pagina_inicial(request):
    descricao = 'Desc dinamica'
    return render(request,'C:/Users/Deus.DEUS.002/PycharmProjects/untitled/templates/home.html',{"desc":descricao})
def login(requests):
    return HttpResponse("BEM VINDO A PÁGINA DE LOGIN")
def registro(requests):
    return HttpResponse("Registro")
