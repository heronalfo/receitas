# Generated by Django 5.0.1 on 2024-01-05 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_alter_users_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.cargos'),
        ),
    ]
