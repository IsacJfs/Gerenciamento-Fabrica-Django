# Generated by Django 4.2.4 on 2023-08-29 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0024_alter_extrusao_hora_fim_alter_extrusao_hora_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrusao',
            name='desperdicio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extrusao',
            name='quantidade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extrusao',
            name='status',
            field=models.CharField(choices=[('iniciado', 'Iniciado'), ('finalizado', 'Finalizado')], default='iniciado', max_length=10),
        ),
        migrations.AddField(
            model_name='extrusao',
            name='tipo_produto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extrusao',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='extrusao',
            name='data_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='extrusao',
            name='hora_fim',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='extrusao',
            name='produto_ingrediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciamento.ingredienteordemservico'),
        ),
        migrations.DeleteModel(
            name='ProdutoExtrusao',
        ),
    ]