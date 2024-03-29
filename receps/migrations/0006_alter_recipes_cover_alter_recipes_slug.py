# Generated by Django 4.2.5 on 2024-03-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receps', '0005_recipes_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='cover',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
