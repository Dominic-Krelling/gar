# Generated by Django 4.1.7 on 2023-06-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gar", "0007_veiculo_modelo"),
    ]

    operations = [
        migrations.AddField(
            model_name="veiculo",
            name="acessorios",
            field=models.ManyToManyField(related_name="veiculos", to="gar.acessorio"),
        ),
    ]