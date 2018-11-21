from django.db import models
from datetime import timedelta

class Pessoa(models.Model):
    nome = models.CharField(max_length=80)
    sexo_choices = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    sexo = models.CharField(max_length=1, choices=sexo_choices)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    categoria_choices = (
        ("COLABORADOR", 'Colaborador'),
        ("BOLSISTA", 'Bolsista'),
        ("MONITOR", 'Monitor'),
        ("INSTRUTOR", 'Instrutor'),
        ("PROFESSOR", 'Professor')
    )
    categoria = models.CharField(max_length=15, choices=categoria_choices)
    carga_horaria = models.TimeField(auto_now=False, null=True, blank=True, verbose_name="Carga horária")
    aulas = models.ForeignKey("Aula", on_delete=models.PROTECT, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True, verbose_name="Observações")

    def __str__(self):
        return self.nome


class Aula(models.Model):
    ritmo = models.CharField(max_length=30)
    professor = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    equipe = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    # limit_choices_to= Pessoa.categoria = 'PROFESSOR',
    duracao_choices = (
        (timedelta(hours=1, minutes=0), '1:00 hora'),
        (timedelta(hours=1, minutes=30), '1:30 horas'),
        (timedelta(hours=2, minutes=0), '2:00 horas'),
    )
    duracao = models.DurationField(default=timedelta, choices=duracao_choices, verbose_name="Duração")
    dia_semana_choices = (
        ("SEGUNDA-FEIRA", 'Segunda-feira'),
        ("TERÇA-FEIRA", 'Terça-feira'),
        ("QUARTA-FEIRA", 'Quarta-feira'),
        ("QUINTA-FEIRA", 'Quinta-feira'),
        ("SEXTA-FEIRA", 'Sexta-feira'),
        ("SÁBADO", 'Sábado'),
        ("DOMINGO", 'Domingo')
    )
    dia_semana = models.CharField(max_length=15, choices=dia_semana_choices, verbose_name="Dia da semana")
    hora_inicio = models.TimeField(auto_now=False, verbose_name="Hora de início")

    def __str__(self):
        return f'{self.ritmo} - {self.dia_semana} ({self.hora_inicio})'