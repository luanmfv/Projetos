from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá Luan, aqui é a pagina polls que você inseriu =D")
