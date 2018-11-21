# Generated by Django 2.1.3 on 2018-11-21 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ritmo', models.CharField(max_length=30)),
                ('duracao', models.TimeField()),
                ('dia_semana', models.CharField(max_length=15)),
                ('hora_inicio', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('COLABORADOR', 'Colaborador'), ('BOLSISTA', 'Bolsista'), ('MONITOR', 'Monitor'), ('INSTRUTOR', 'Instrutor'), ('PROFESSOR', 'Professor')], max_length=15)),
                ('carga_horaria', models.TimeField(blank=True, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('aulas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tm.Aula')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tm.Pessoa'),
        ),
    ]