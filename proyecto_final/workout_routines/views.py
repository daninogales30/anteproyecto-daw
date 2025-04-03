from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from workout_routines.forms import WorkoutForm, RoutineExerciseForm
from workout_routines.models import RoutineExercise


class WorkoutFormView(FormView):
    form_class = WorkoutForm
    template_name = 'workout_routine/form.html'
    success_url = reverse_lazy('persons:list')
    
    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear entrenamiento'
        return context


class RoutineFormView(FormView):
    form_class = RoutineExerciseForm
    template_name = 'workout_routine/form.html'
    success_url = reverse_lazy('persons:list')

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear rutina'
        return context

class RoutineListView(ListView):
    model = RoutineExercise
    template_name = 'workout_routine/list.html'
    context_object_name = 'routines'
