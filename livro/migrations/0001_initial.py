# Generated by Django 4.2.4 on 2023-08-28 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionariosdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Livrosdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('disponibilidade', models.BooleanField(default=True)),
                ('img_livro', models.BinaryField()),
                ('ISBN', models.CharField(max_length=100)),
                ('data_cadastro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuariosdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=30)),
                ('matricula', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimosdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateTimeField()),
                ('data_retorno', models.DateTimeField()),
                ('situacao', models.CharField(max_length=30)),
                ('id_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.funcionariosdb')),
                ('id_livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.livrosdb')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.usuariosdb')),
            ],
        ),
    ]
