# Generated by Django 4.2.8 on 2023-12-11 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_voo', models.CharField(max_length=10)),
                ('origem', models.CharField(default='Petrolina', max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('data_partida', models.CharField(max_length=10)),
                ('data_chegada', models.CharField(blank=True, max_length=10, null=True)),
                ('nome', models.CharField(max_length=50)),
                ('classe', models.CharField(default='econômica', max_length=10)),
            ],
        ),
    ]