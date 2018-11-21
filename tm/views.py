from django.shortcuts import render
from tm.models import Pessoa, Aula
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


# PESSOA
class PessoaCreateView(CreateView):
    model = Pessoa
    fields = ['nome', 'sexo', 'categoria', 'telefone']


class PessoaDetailView(DetailView):
    model = Pessoa


class PessoaListView(ListView):
    model = Pessoa


class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = ['categoria', 'aulas']


class PessoaDeleteView(DeleteView):
    model = Pessoa


# AULA
class AulaCreateView(CreateView):
    model = Aula
    fields = ['ritmo', 'professor', 'dia_semana', 'hora_inicio', 'duracao']

class AulaDetailView(DetailView):
    model = Aula


class AulaListView(ListView):
    model = Aula


class AulaUpdateView(UpdateView):
    model = Aula
    fields = ['ritmo', 'dia_semana', 'hora_inicio']


class AulaDeleteView(DeleteView):
    model = Aula