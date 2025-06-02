from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.db.models import Count, Q, Case, When, IntegerField
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, DetailView, UpdateView
from rest_framework import generics

from persons.forms import PersonForm, PersonUpdateForm
from persons.models import Person
from persons.serializers import LeaderboardSerializer
from workout_routines.models import Workout


class PersonRegisterCreateView(FormView):
    template_name = 'registration/register.html'
    form_class = PersonForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('persons:index')

    def form_valid(self, form):
        person = form.save(commit=False)
        person.set_password(form.cleaned_data['password'])
        try:
            grasa = person.calculate_bodyfat_percentage()
        except ValueError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)

        person.body_fat_percentage = grasa

        try:
            imc = person.calculate_imc()
        except ValueError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)

        person.imc = imc

        try:
            day_calories = person.calculate_diary_callories()
        except ValueError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)

        person.diary_callories = day_calories
        person.save()
        return super().form_valid(form)


class PersonLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class PersonLogoutView(LogoutView):
    template_name = 'registration/logout.html'


class PersonIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'persons/index.html'


class PersonDetailView(LoginRequiredMixin, DetailView):
    template_name = 'persons/detail.html'
    model = Person
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "persons/update.html"
    model = Person
    form_class = PersonUpdateForm
    success_url = reverse_lazy('persons:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        person = form.save(commit=False)
        changed = set(form.changed_data)

        bf_fields = {'height', 'cintura', 'cuello', 'cadera', 'gender'}
        if changed & bf_fields:
            try:
                person.body_fat_percentage = person.calculate_bodyfat_percentage()
            except ValueError as e:
                # Si falta algún dato o es inválido, devolvemos el formulario con el error
                form.add_error(None, str(e))
                return self.form_invalid(form)

        if changed & {'height', 'weight'}:
            person.imc = person.calculate_imc()

        calorie_fields = {'gender', 'weight', 'height', 'edad', 'activity_level', 'fitness_goal'}
        if changed & calorie_fields:
            try:
                person.diary_callories = person.calculate_diary_callories()
            except ValueError as e:
                form.add_error(None, str(e))
                return self.form_invalid(form)

        person.save()
        return super().form_valid(form)


class PersonPasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'persons/password.html'
    model = Person
    form_class = PasswordChangeForm
    success_url = reverse_lazy('persons:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        logout(self.request)
        return super().form_valid(form)


class PersonWorkoutListView(LoginRequiredMixin, DetailView):
    model = Person
    template_name = 'persons/workout_list.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.object

        dias_orden = Case(
            When(name='lunes', then=1),
            When(name='martes', then=2),
            When(name='miércoles', then=3),
            When(name='jueves', then=4),
            When(name='viernes', then=5),
            When(name='sábado', then=6),
            When(name='domingo', then=7),
            output_field=IntegerField()
        )

        workouts_ordenados = (
            Workout.objects
            .filter(user=usuario)
            .annotate(orden_dia=dias_orden)
            .order_by('orden_dia')
        )

        context['workouts_ordenados'] = workouts_ordenados
        return context


class PersonLeaderboardAPIView(generics.ListAPIView):
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        q = Person.objects.annotate(total_workouts=Count('user_workouts',
                                                         filter=Q(user_workouts__exercises__isnull=False),
                                                         distinct=True)).order_by('-total_workouts')
        return q[:5]


class PersonLeaderboardTemplate(TemplateView):
    template_name = 'persons/api_ranking.html'
