from django.contrib import admin

from diets.models import FoodItem, SemanalDiet, DayDiet, Day

admin.site.register(FoodItem)
admin.site.register(SemanalDiet)
admin.site.register(DayDiet)
admin.site.register(Day)

