# Generated by Django 4.1 on 2022-11-22 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('carrera', models.CharField(max_length=50)),
                ('puntuacion', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
