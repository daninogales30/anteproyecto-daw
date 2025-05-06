import math

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import User, AbstractUser

from diets.models import SemanalDiet
from workout_routines.models import Workout


class Person(AbstractUser):
    birth_date = models.DateField("Fecha de nacimiento", null=True, blank=True)
    edad = models.PositiveIntegerField("Edad", default=18)
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
    height = models.IntegerField("Altura (cm)", help_text="Altura en centímetros", default=170)
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
        default='maintain',
        null=True,
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
    diary_callories = models.PositiveIntegerField("Calorías diarias", null=True, blank=True, default=0)



    def calculate_bodyfat_percentage(self):
        if not self.height or self.height <= 0:
            raise ValueError("Altura no puede ser cero o negativa")
        if self.gender == 'M':
            diff = self.cintura - self.cuello
            if diff <= 0:
                raise ValueError("Perímetro cintura-cuello debe ser > 0 para hombre")
            denom = 1.0324 - 0.19077 * math.log10(diff) + 0.15456 * math.log10(self.height)
            bodyfat = (495 / denom) - 450

        else:
            diff = self.cintura + self.cadera - self.cuello
            if diff <= 0:
                raise ValueError("Perímetro cintura+cadera-cuello debe ser > 0 para mujer")
            denom = 1.29579 - 0.35004 * math.log10(diff) + 0.22100 * math.log10(self.height)
            bodyfat = (495 / denom) - 450

        return round(bodyfat, 2)



    def calculate_imc(self):
        imc = self.weight / ((self.height / 100) ** 2)
        return round(imc, 1)

    def calculate_diary_callories(self):
        if self.gender == 'M':
            tmb = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.edad)
        else:
            tmb = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.edad)

        if self.activity_level == 'sedentary':
            tmb_final = tmb * 1.2
        elif self.activity_level == 'light':
            tmb_final = tmb * 1.375
        elif self.activity_level == 'moderate':
            tmb_final = tmb * 1.55
        else:
            tmb_final = tmb * 1.725

        return round(tmb_final, 0)

    def total_workouts(self):
        return self.user_workouts.count()

