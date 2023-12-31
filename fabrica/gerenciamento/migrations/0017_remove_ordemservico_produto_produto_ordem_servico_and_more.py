# Generated by Django 4.2.4 on 2023-08-27 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0016_rename_data_ordemservico_data_inicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservico',
            name='produto',
        ),
        migrations.AddField(
            model_name='produto',
            name='ordem_servico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='gerenciamento.ordemservico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
