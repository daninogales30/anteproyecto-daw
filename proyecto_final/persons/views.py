from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, DetailView, UpdateView, ListView
from persons.forms import PersonForm, PersonUpdateForm
from persons.models import Person


class PersonRegisterCreateView(FormView):
    template_name = 'registration/register.html'
    form_class = PersonForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('persons:index')

    def form_valid(self, form):
        person = form.save(commit=False)
        person.set_password(form.cleaned_data['password'])
        # grasa = person.calculate_bodyfat_percentage()
        # person.body_fat_percentage = grasa

        imc = person.calculate_imc()
        person.imc = imc

        day_calories = person.calculate_day_calories()
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

        # if 'height' in form.changed_data or 'cintura' in form.changed_data or 'cuello' in form.changed_data or 'cadera' in form.changed_data or 'gender' in form.changed_data:
            # body_fat_percentage = person.calculate_bodyfat_percentage()
            # person.body_fat_percentage = body_fat_percentage

        if 'height' in form.changed_data or 'weight' in form.changed_data:
            imc = person.calculate_imc()
            person.imc = imc

        if 'gender' in form.changed_data or 'weight' in form.changed_data or 'height' in form.changed_data or 'edad' in form.changed_data or 'activity_level' in form.changed_data:
            day_calories = person.calculate_diary_callories()
            person.diary_callories = day_calories

        person.save()
        return super().form_valid(form)


class PersonPasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'persons/password.html'
    model = Person
    form_class = PasswordChangeForm
    success_url = reverse_lazy('persons:profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PersonWorkoutListView(LoginRequiredMixin, DetailView):
    model = Person
    template_name = 'persons/workout_list.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user
