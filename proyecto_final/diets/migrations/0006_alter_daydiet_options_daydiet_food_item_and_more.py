# Generated by Django 5.2 on 2025-04-29 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0005_alter_semanaldiet_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daydiet',
            options={'ordering': ['date', 'moment']},
        ),
        migrations.AddField(
            model_name='daydiet',
            name='food_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='diets.fooditem', verbose_name='Alimento'),
        ),
        migrations.AddField(
            model_name='daydiet',
            name='moment',
            field=models.CharField(blank=True, choices=[('desayuno', 'Desayuno'), ('almuerzo', 'Almuerzo'), ('merienda', 'Merienda'), ('cena', 'Cena')], max_length=10, null=True, verbose_name='Momento'),
        ),
        migrations.AddField(
            model_name='daydiet',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Observaciones'),
        ),
        migrations.AddField(
            model_name='daydiet',
            name='quantity_g',
            field=models.PositiveIntegerField(default=100, verbose_name='Cantidad (g)'),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='daydiet',
            name='semanal_diet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='diets.semanaldiet'),
        ),
        migrations.AlterField(
            model_name='daydiet',
            name='total_calories',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Calorías totales'),
        ),
        migrations.AlterUniqueTogether(
            name='daydiet',
            unique_together={('semanal_diet', 'date', 'moment', 'food_item')},
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]
