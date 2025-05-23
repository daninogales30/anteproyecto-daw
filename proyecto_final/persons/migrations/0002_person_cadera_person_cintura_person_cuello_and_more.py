# Generated by Django 5.1.7 on 2025-04-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cadera',
            field=models.FloatField(default=0, max_length=20, verbose_name='Perímetro cadera (Rellenar solo si eres mujer) (cm) '),
        ),
        migrations.AddField(
            model_name='person',
            name='cintura',
            field=models.FloatField(default=0, max_length=20, verbose_name='Perímetro cintura (cm) '),
        ),
        migrations.AddField(
            model_name='person',
            name='cuello',
            field=models.FloatField(default=0, max_length=20, verbose_name='Perímetro cuello (cm) '),
        ),
        migrations.AddField(
            model_name='person',
            name='imc',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Género'),
        ),
    ]
