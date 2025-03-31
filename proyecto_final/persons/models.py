from django.db import models
from django.contrib.auth.models import User, AbstractUser

from diets.models import SemanalDiet


class Person(AbstractUser):
    birth_date = models.DateField("Fecha de nacimiento", null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    FITNESS_GOAL_CHOICES = [
        ('lose_weight', 'Perder peso'),
        ('gain_muscle', 'Ganar músculo'),
        ('maintain', 'Mantenimiento'),
        ('improve_endurance', 'Mejorar resistencia'),
    ]
    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Sedentario'),
        ('light', 'Ligero (ejercicio 1-3 días/semana)'),
        ('moderate', 'Moderado (3-5 días/semana)'),
        ('active', 'Activo (6-7 días/semana)'),
    ]
    diets = models.ManyToManyField(SemanalDiet)
    gender = models.CharField("Género", max_length=1, choices=GENDER_CHOICES, blank=True)
    weight = models.FloatField("Peso (kg)", help_text="Peso en kilogramos", default=70.0)
    height = models.FloatField("Altura (cm)", help_text="Altura en centímetros", default=170.0)
    body_fat_percentage = models.FloatField(
        "Porcentaje de grasa corporal",
        null=True,
        blank=True,
        help_text="Ej: 15.5 (opcional)"
    )
    fitness_goal = models.CharField(
        "Objetivo principal",
        max_length=20,
        choices=FITNESS_GOAL_CHOICES,
        default='maintain'
    )
    activity_level = models.CharField(
        "Nivel de actividad",
        max_length=10,
        choices=ACTIVITY_LEVEL_CHOICES,
        default='moderate'
    )
    allergies = models.TextField("Alergias alimenticias", blank=True)
    medical_conditions = models.TextField("Condiciones médicas", blank=True)
    target_weight = models.FloatField("Peso objetivo (kg) (Dejar en blanco si tu objetivo es mantenimiento)", null=True, blank=True)
    profile_picture = models.ImageField(
        "Foto de perfil",
        upload_to='profile_pics/',
        blank=True,
        default='profile_pics/default.jpg'
    )
    bio = models.TextField("Biografía", max_length=500, blank=True)
