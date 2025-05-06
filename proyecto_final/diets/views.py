from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, DeleteView, DetailView

from diets.forms import SemanalDietForm, FoodItemForm, DayDietForm, DayForm
from diets.models import SemanalDiet, DayDiet


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


class DayFormView(LoginRequiredMixin, FormView):
    form_class = DayForm
    template_name = 'diets/form.html'
    success_url = reverse_lazy('persons:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        day = form.save(commit=False)
        day.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear día semanal'
        return context


class DayDietFormView(LoginRequiredMixin, FormView):
    form_class = DayDietForm
    template_name = 'diets/form.html'
    success_url = reverse_lazy('persons:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        daydiet = form.save(commit=False)
        daydiet.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Añadir alimentos a la dieta'
        return context


class PersonDietListView(LoginRequiredMixin, ListView):
    model = SemanalDiet
    template_name = 'diets/person_diets.html'
    context_object_name = 'semanal_diets'

    def get_queryset(self):
        user = self.request.user
        queryset = SemanalDiet.objects.filter(user=user)
        return queryset


class PersonDietDetailView(LoginRequiredMixin, DetailView):
    model = SemanalDiet
    template_name = 'diets/details.html'
    context_object_name = 'semanal_diet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        semanal_diet = self.object

        dias_ordenados = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        dias_con_dietas = []

        for dia in dias_ordenados:
            day_obj = semanal_diet.days.filter(day=dia).first()
            if day_obj:
                diets = day_obj.day_diets.all().order_by('moment')
                dias_con_dietas.append({
                    'nombre': dia.capitalize(),
                    'diets': diets,
                    'total_calories': day_obj.total_calories,
                })

        context['dias_con_dietas'] = dias_con_dietas
        context['usuario'] = user
        context['total_calories'] = semanal_diet.total_calories()
        return context


class PersonDietDeleteView(LoginRequiredMixin, DeleteView):
    model = SemanalDiet
    template_name = "diets/person_deletediet.html"
    context_object_name = "semanal_diet"
    success_url = reverse_lazy('diets:list_semanaldiets')


class PersonDayDietDeleteView(LoginRequiredMixin, DeleteView):
    model = DayDiet
    template_name = "diets/person_deletedaydiet.html"
    context_object_name = "daydiet"
    success_url = reverse_lazy('diets:list_semanaldiets')


class FoodItemFormView(LoginRequiredMixin, FormView):
    form_class = FoodItemForm
    template_name = 'diets/form.html'
    success_url = reverse_lazy('persons:index')

    def form_valid(self, form):
        food_item = form.save(commit=False)
        user = self.request.user

        if user.user_fooditem.filter(name=food_item.name).exists():
            messages.error(self.request,
                           f"Ya tienes un alimento con ese nombre")
            return self.form_invalid(form)

        food_item.user = user
        food_item.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Añadir alimento'
        return context
