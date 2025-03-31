from django.db import models


class SemanalDiet(models.Model):
    start_date = models.DateField("Inicio de semana")
    finish_date = models.DateField("Fin de semana")
    goal = models.CharField("Objetivo de la semana", max_length=100, blank=True)


    def __str__(self):
        return f"Semana {self.start_date} al {self.finish_date}"


class DayDiet(models.Model):
    DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    semanal_diet = models.ForeignKey(SemanalDiet, on_delete=models.CASCADE, related_name='dias')
    date = models.DateField("Fecha específica")
    day = models.CharField("Día", max_length=15, choices=DIAS_SEMANA)
    total_calories = models.PositiveIntegerField("Calorías totales", default=0)


class Food(models.Model):
    FOOD_TYPE = [
        ('desayuno', 'Desayuno'),
        ('almuerzo', 'Almuerzo'),
        ('merienda', 'Merienda'),
        ('cena', 'Cena'),
    ]

    day = models.ForeignKey(DayDiet, on_delete=models.CASCADE, related_name='comidas')
    type = models.CharField("Tipo de comida", max_length=10, choices=FOOD_TYPE)
    food = models.JSONField("Alimentos consumidos")  # Ej: {"Pollo": "200g", "Arroz": "150g"}
    notes = models.TextField("Observaciones", blank=True)
    total_calories_per_food = models.PositiveIntegerField("Calorías totales", default=0)

    def __str__(self):
        return f"{self.type} - {self.day.date}"
