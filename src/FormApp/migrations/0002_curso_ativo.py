# Generated by Django 4.1.1 on 2023-02-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]