# Generated by Django 4.1 on 2022-09-27 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedido_APP', '0002_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nropedido', models.IntegerField()),
                ('fecha', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
    ]