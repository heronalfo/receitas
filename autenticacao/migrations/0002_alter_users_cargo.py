# Generated by Django 5.0.1 on 2024-01-05 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.cargos'),
        ),
    ]
