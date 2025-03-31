from django.contrib import admin

from workout_routines.models import *

admin.site.register(MuscleGroup)
admin.site.register(Equipment)
admin.site.register(Exercise)
admin.site.register(RoutineExercise)
admin.site.register(Workout)
