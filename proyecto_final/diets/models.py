from django.db import models


class SemanalDiet(models.Model):
    user = models.ForeignKey(
        'persons.Person',
        on_delete=models.CASCADE,
        related_name='user_semanaldiets',
        null=True,
        blank=True
    )
    name = models.CharField(verbose_name='Nombre, ej: Semana 1', max_length=100, default='Semana 1')
    precargado = models.BooleanField(default=False)
    start_date = models.DateField("Inicio de semana")
    finish_date = models.DateField("Fin de semana")

    class Meta:
        unique_together = [('user', 'name')]

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


class FoodItem(models.Model):
    name = models.CharField("Nombre", max_length=100, unique=True)
    calories_per_100g = models.PositiveIntegerField("Calorías (por 100g)")
    CATEGORY_CHOICES = [
        ('fruta', 'Fruta'),
        ('verdura', 'Verdura'),
        ('lácteo', 'Lácteo'),
        ('cereal', 'Cereal'),
        ('otro', 'Otro'),
    ]
    category = models.CharField("Categoría", max_length=20, choices=CATEGORY_CHOICES, default='otro')

    def __str__(self):
        return f"{self.name} ({self.calories_per_100g} kcal/100g)"


class Food(models.Model):
    FOOD_TYPE = [
        ('desayuno', 'Desayuno'),
        ('almuerzo', 'Almuerzo'),
        ('merienda', 'Merienda'),
        ('cena', 'Cena'),
    ]

    day = models.ForeignKey(DayDiet, on_delete=models.CASCADE, related_name='comidas')
    type = models.CharField("Tipo de comida", max_length=10, choices=FOOD_TYPE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT, verbose_name="Alimento", null=True, blank=True)
    notes = models.TextField("Observaciones", blank=True)
    total_calories_per_food = models.PositiveIntegerField("Calorías totales", default=0)

    def __str__(self):
        return f"{self.type} - {self.day.date}"
