from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView, TemplateView

from blog.forms import EntradaForm
from blog.models import Entrada

class BlogTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/index.html'


class EntradaListView(LoginRequiredMixin, ListView):
    model = Entrada
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class EntradaFormView(LoginRequiredMixin, FormView):
    model = Entrada
    template_name = 'blog/form.html'
    form_class = EntradaForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        entrada = form.save(commit=False)
        entrada.user = self.request.user
        entrada.save()

        return super().form_valid(form)

