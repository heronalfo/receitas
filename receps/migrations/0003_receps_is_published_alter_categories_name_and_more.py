# Generated by Django 5.0.1 on 2024-01-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receps', '0002_categories_remove_users_cargo_receps_delete_cargos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receps',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(blank=True, max_length=38, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='receps',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
