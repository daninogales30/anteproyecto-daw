from django import forms

from workout_routines.models import RoutineExercise, Workout


class RoutineExerciseForm(forms.ModelForm):
    class Meta:
        model = RoutineExercise
        fields = ['workout', 'exercise', 'sets', 'reps', 'rest_time']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtenemos el usuario desde las kwargs
        super(RoutineExerciseForm, self).__init__(*args, **kwargs)
        if user:
            # Filtramos los workouts por el usuario actual
            self.fields['workout'].queryset = Workout.objects.filter(user=user)

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']