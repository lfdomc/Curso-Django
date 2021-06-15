from django.shortcuts import render

# Create your views here.
from django.views.generic import *


class PruebaView(TemplateView):
    template_name = "home/prueba.html"

    
class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name ="listaNumeros"
    queryset = ["1","11","111","1111"]
