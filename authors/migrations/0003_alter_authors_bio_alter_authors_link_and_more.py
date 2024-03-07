# Generated by Django 4.2.5 on 2024-02-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_authors_is_professional_alter_authors_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='bio',
            field=models.CharField(default='No bio yet', max_length=100),
        ),
        migrations.AlterField(
            model_name='authors',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='name',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
    ]
