from django.shortcuts import render
from django.views.generic import TemplateView


class DietTemplateView(TemplateView):
    template_name = 'diets/diets.html'
