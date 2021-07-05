from django.contrib import admin
from django.urls import path
from . import views

def DesdeApps(self):
         print("hola mundo")

urlpatterns = [
    
    path("new-departamento/", views.NewDepartamentoView.as_view(), name= "prueba_add"),
]