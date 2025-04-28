from django.urls import path

from diets.views import DietTemplateView

app_name = 'diets'

urlpatterns = [
    path("", DietTemplateView.as_view(), name="index"),
]