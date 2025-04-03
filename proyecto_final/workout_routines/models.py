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
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise, through=RoutineExercise)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name