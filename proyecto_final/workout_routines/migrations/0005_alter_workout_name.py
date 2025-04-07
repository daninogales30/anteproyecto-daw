# Generated by Django 5.2 on 2025-04-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_routines', '0004_workout_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miércoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sábado', 'Sábado'), ('domingo', 'Domingo')], max_length=100),
        ),
    ]
