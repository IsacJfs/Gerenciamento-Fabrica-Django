# Generated by Django 4.2.4 on 2023-08-24 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corte',
            old_name='cutting_machine',
            new_name='maquina_corte',
        ),
        migrations.RenameField(
            model_name='impressao',
            old_name='printing_machine',
            new_name='maquina_impressao',
        ),
    ]
