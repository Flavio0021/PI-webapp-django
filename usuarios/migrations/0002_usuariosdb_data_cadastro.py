# Generated by Django 4.2.4 on 2023-10-18 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariosdb',
            name='data_cadastro',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
