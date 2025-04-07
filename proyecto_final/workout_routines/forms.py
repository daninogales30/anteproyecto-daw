from django import forms

from workout_routines.models import RoutineExercise, Workout


class RoutineExerciseForm(forms.ModelForm):
    class Meta:
        model = RoutineExercise
        fields = ['workout', 'exercise', 'sets', 'reps', 'rest_time']

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']