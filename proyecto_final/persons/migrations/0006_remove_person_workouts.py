# Generated by Django 5.2 on 2025-04-04 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_alter_person_diets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='workouts',
        ),
    ]
