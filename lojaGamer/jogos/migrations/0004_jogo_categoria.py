# Generated by Django 2.2.12 on 2020-05-28 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0003_auto_20200528_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jogos.Categoria'),
        ),
    ]
