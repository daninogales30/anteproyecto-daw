from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.asgi import get_asgi_application
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView, DetailView
from persons.forms import PersonForm
from persons.models import Person


class PersonRegisterCreateView(FormView):
    template_name = 'registration/register.html'
    form_class = PersonForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('persons:index')

    def form_valid(self, form):
        person = form.save(commit=False)
        person.set_password(form.cleaned_data['password'])
        grasa = person.calculate_bodyfat_percentage()
        person.body_fat_percentage = grasa
        person.save()
        return super().form_valid(form)

class PersonLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class PersonIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'persons/index.html'

class PersonDetailView(LoginRequiredMixin, DetailView):
    template_name = 'persons/detail.html'
    model = Person
    context_object_name = 'usuario'


    def get_object(self):
        return self.request.user



