# Generated by Django 2.1.5 on 2019-03-11 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0012_jornada_jornada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='jornada',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('1000', '1000')], max_length=4),
        ),
    ]
