# Generated by Django 5.1.7 on 2025-04-03 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_routines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='video_url',
        ),
    ]
