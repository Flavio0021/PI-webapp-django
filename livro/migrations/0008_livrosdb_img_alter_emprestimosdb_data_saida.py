# Generated by Django 4.2.5 on 2023-10-03 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0007_alter_emprestimosdb_data_retorno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livrosdb',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_livro'),
        ),
        migrations.AlterField(
            model_name='emprestimosdb',
            name='data_saida',
            field=models.DateField(default=datetime.date(2023, 10, 2)),
        ),
    ]