# Generated by Django 4.2.4 on 2023-08-24 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0006_rename_tipomaterial_ordemservico_tipo_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientes',
            old_name='ingrediente_1',
            new_name='ingrediente',
        ),
        migrations.RenameField(
            model_name='tinta',
            old_name='cor_1',
            new_name='cor',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_10',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_11',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_12',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_2',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_3',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_4',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_5',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_6',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_7',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_8',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='ingrediente_9',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_10',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_11',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_12',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_2',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_3',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_4',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_5',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_6',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_7',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_8',
        ),
        migrations.RemoveField(
            model_name='tinta',
            name='cor_9',
        ),
    ]