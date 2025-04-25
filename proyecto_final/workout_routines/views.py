from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, DeleteView
from workout_routines.forms import RoutineExerciseForm, WorkoutExerciseForm
from workout_routines.models import RoutineExercise, Workout


class WorkoutFormView(LoginRequiredMixin, FormView):
    form_class = WorkoutExerciseForm
    template_name = 'workout_routine/form.html'
    success_url = reverse_lazy('persons:index')

    def form_valid(self, form):
        workout_day = form.save(commit=False)
        user = self.request.user

        if user.user_workouts.filter(name=workout_day.name).exists():
            messages.error(self.request,
                           f"Ya tienes un entrenamiento programado para este dia.")
            return self.form_invalid(form)

        workout_day.save()
        user.user_workouts.add(workout_day)

        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear entrenamiento'
        return context

class RoutineFormView(LoginRequiredMixin, FormView):
    form_class = RoutineExerciseForm
    template_name = 'workout_routine/form.html'
    success_url = reverse_lazy('persons:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        routine = form.save(commit=False)
        routine.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear rutina'
        return context


class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = 'workout_routine/detail.html'
    context_object_name = 'workout'

    def get_queryset(self):
        return self.request.user.user_workouts.all()

class PreloadedWorkoutsListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'workout_routine/preloaded.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        queryset = Workout.objects.filter(precargado=True)
        return queryset

class RoutineDeleteView(LoginRequiredMixin, DeleteView):
    model = RoutineExercise
    template_name = 'workout_routine/delete.html'
    context_object_name = 'routine'
    success_url = reverse_lazy('persons:workouts-list')
