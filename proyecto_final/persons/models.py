import math

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import User, AbstractUser

from diets.models import SemanalDiet
from workout_routines.models import Workout


class Person(AbstractUser):
    birth_date = models.DateField("Fecha de nacimiento", null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    cuello = models.FloatField("Perímetro cuello (cm) ", max_length=20, default=0)
    cadera = models.FloatField("Perímetro cadera (Rellenar solo si eres mujer) (cm) ", max_length=20, default=0)
    cintura = models.FloatField("Perímetro cintura (cm) ", max_length=20, default=0)
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
    diets = models.ManyToManyField(SemanalDiet, blank=True)
    gender = models.CharField("Género", max_length=1, choices=GENDER_CHOICES, blank=True)
    weight = models.FloatField("Peso (kg)", help_text="Peso en kilogramos", default=70.0)
    height = models.FloatField("Altura (cm)", help_text="Altura en centímetros", default=170.0)
    body_fat_percentage = models.FloatField(
        "Porcentaje de grasa corporal",
        null=True,
        blank=True,
        help_text="Ej: 15.5 (opcional)"
    )
    imc = models.FloatField(default=0)
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

    def calculate_bodyfat_percentage(self):
        if self.gender == 'M':
            return round(number=(495/1.0324-0.19077*math.log10(self.cintura-self.cuello)+0.15456*math.log10(self.height)) - 450,ndigits=2)
        return round(number=(495/1.29579 - 0.35004*math.log10(self.cintura+self.cadera-self.cuello)+0.22100*math.log10(self.height)) - 450, ndigits=2)

    def calculate_imc(self):
        if self.gender == 'M':
            pass
