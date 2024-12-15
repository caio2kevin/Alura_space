from django.shortcuts import render

def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina", "legenda": "Uma nebulosa incrível!"},
        2: {"nome": "Galáxia NGC", "legenda": "Uma galáxia deslumbrante!"},
    }

    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
