# Generated by Django 2.1.5 on 2019-03-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0008_game_jornada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='tipo',
            field=models.CharField(choices=[('IZ', 'InterZona'), ('Z', 'Zona')], max_length=20),
        ),
    ]
