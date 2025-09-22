Criar uma API integrada ao mysql, usando django

dentro da pasta fullstack, usei o comando  django-admin startproject mysite fullstack

django-admin (usa a função adm) startproject (inicia o projeto) (mysite) nome da pasta aonde o django colocará a estrtura

fullstack nome da pasta

django-admin startproject nome_da_pasta_da_estrutura pasta_criada_para_o_projeto

-------------------------------------------------------------------------------------------------------------------------

python manage.py startapp polls

Para criar seu aplicativo

Escreva sua primeira visualização

Vamos escrever a primeira visualização. Abra o arquivo e coloque o seguinte código Python nele:polls/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



