from django.contrib import messages
from django.contrib.auth import user_logged_in
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, CreateView, DeleteView

from diets.forms import SemanalDietForm
from diets.models import SemanalDiet
from persons.models import Person


class DietTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'diets/diets.html'

class SemanalDietFormView(LoginRequiredMixin, FormView):
    form_class = SemanalDietForm
    template_name = 'diets/form.html'
    success_url = reverse_lazy('persons:index')

    def form_valid(self, form):
        semanal_diet = form.save(commit=False)
        user = self.request.user

        if user.user_semanaldiets.filter(name=semanal_diet.name).exists():
            messages.error(self.request,
                           f"Ya tienes una dieta semanal con ese nombre")
            return self.form_invalid(form)

        semanal_diet.user = user
        semanal_diet.save()
        user.user_semanaldiets.add(semanal_diet)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear dieta semanal'
        return context

class PersonDietListView(LoginRequiredMixin, ListView):
    model = SemanalDiet
    template_name = 'diets/person_diets.html'
    context_object_name = 'semanal_diets'

    def get_queryset(self):
        user = self.request.user
        queryset = SemanalDiet.objects.filter(user=user)
        return queryset

class PersonDietDeleteView(LoginRequiredMixin, DeleteView):
    model = SemanalDiet
    template_name = "diets/person_deletediet.html"
    context_object_name = "semanal_diet"
    success_url = reverse_lazy('diets:list_semanaldiets')