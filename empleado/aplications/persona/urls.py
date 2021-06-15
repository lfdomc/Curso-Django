from django.contrib import admin
from django.urls import path

def DesdeApps(self):
         print("hola mundo")

urlpatterns = [
    path("persona/", DesdeApps),
]