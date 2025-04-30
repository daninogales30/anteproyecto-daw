from django.db import models
from django.db.models import Sum


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

    def total_calories(self):
        result = self.meals.aggregate(total=Sum('total_calories'))['total']
        return result or 0


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
    notes = models.TextField("Observaciones", blank=True)
    user = models.ForeignKey(
        'persons.Person',
        on_delete=models.CASCADE,
        related_name='user_fooditem',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.calories_per_100g} kcal/100g)"


class Day(models.Model):
    DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    semanal_diet = models.ForeignKey(
        SemanalDiet,
        on_delete=models.CASCADE,
        related_name='days',
        null=True,
        blank=True
    )

    day = models.CharField(
        'Día',
        max_length=15,
        choices=DIAS_SEMANA
    )

    class Meta:
        unique_together = [('semanal_diet', 'day')]
        ordering = ['day']

    def __str__(self):
        return f"{self.day} ({self.semanal_diet})"


class DayDiet(models.Model):
    MOMENTO_DIA = [
        ('desayuno', 'Desayuno'),
        ('almuerzo', 'Almuerzo'),
        ('merienda', 'Merienda'),
        ('cena', 'Cena'),
    ]

    semanal_diet = models.ForeignKey(
        SemanalDiet,
        on_delete=models.CASCADE,
        related_name='meals'
    )

    day = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        related_name='day_diets',
        null=True,
        blank=True
    )

    moment = models.CharField(
        'Momento',
        max_length=10,
        choices=MOMENTO_DIA,
        null=True,
        blank=True
    )
    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.PROTECT,
        verbose_name='Alimento',
        null=True,
        blank=True
    )
    quantity_g = models.PositiveIntegerField(
        'Cantidad (g)',
        default=100
    )
    total_calories = models.PositiveIntegerField(
        'Calorías totales',
        default=0,
        editable=False
    )
    notes = models.TextField('Observaciones', blank=True)

    class Meta:
        unique_together = [
            ('semanal_diet', 'moment', 'food_item')
        ]
        ordering = ['moment']

    def save(self, *args, **kwargs):
        # Calcular calorías totales automáticamente
        self.total_calories = (
                self.food_item.calories_per_100g * self.quantity_g // 100
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.day} {self.moment} {self.food_item.name}"
        )
