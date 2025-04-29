from django.contrib import admin

from diets.models import FoodItem, SemanalDiet, DayDiet

admin.site.register(FoodItem)
admin.site.register(SemanalDiet)
admin.site.register(DayDiet)

