from contextlib import nullcontext

from django.db import models


class MuscleGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_groups = models.ManyToManyField(MuscleGroup)
    equipment_needed = models.ManyToManyField(Equipment, blank=True)

    def __str__(self):
        return self.name

class RoutineExercise(models.Model):
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField("Series", default=3)
    reps = models.PositiveIntegerField("Repeticiones", default=10)
    rest_time = models.PositiveIntegerField("Descanso entre series (segundos)", default=60)

    class Meta:
        unique_together = [('workout', 'exercise')]

    def __str__(self):
        return f"{self.exercise.name} en {self.workout.name}"

class Workout(models.Model):
    DIAS_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    NIVEL_DIFICULTAD = [
        ('principiante', 'Principiante'),
        ('amateur', 'Amateur'),
        ('avanzado', 'Avanzado'),
        ('elite', 'Elite'),
        ('culturista', 'Culturista'),
    ]

    name = models.CharField(max_length=100, choices=DIAS_SEMANA)
    exercises = models.ManyToManyField(Exercise, through=RoutineExercise)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'persons.Person',
        on_delete=models.CASCADE,
        related_name='user_workouts',
        null=True,
        blank=True
    )
    precargado = models.BooleanField(default=False)
    # nivel = models.CharField(choices=NIVEL_DIFICULTAD, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name