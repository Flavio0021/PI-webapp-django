# Generated by Django 4.2.4 on 2023-10-12 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0011_alter_emprestimosdb_data_retorno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimosdb',
            name='id_funcionario',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.funcionariosdb'),
        ),
    ]
