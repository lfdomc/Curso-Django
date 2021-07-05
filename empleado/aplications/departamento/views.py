from django.shortcuts import render
from django.views.generic.edit import(FormView) 
from django.urls import reverse_lazy

from .forms import NewDepartamentoForm
from aplications.persona.models import Empleado
from .models import Departamento

class NewDepartamentoView(FormView):

    template_name = "departamento/new-departamento.html"
    form_class = NewDepartamentoForm
    success_url = "/"

    def form_valid(self, form):
        depa = Departamento(
           name=form.cleaned_data["departamento"],
           shor_name =form.cleaned_data["shor_name"]

        )
        depa.save()

        nombre = form.cleaned_data["nombre"]
        apellido = form.cleaned_data["apellidos"]
        Empleado.objects.create(
           first_name=nombre, 
           last_name=apellido,
           job= 1,
           departamento=depa

        )


        return super(NewDepartamentoView,self).form_valid(form)