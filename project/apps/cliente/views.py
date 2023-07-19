from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

# Create your views here.


from . import forms, models


class ClienteList(ListView):
    model = models.Cliente


class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")

class ClienteDetail(DetailView):
    model = models.Cliente

class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente:cliente_list")


class ClienteDelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:cliente_list")
