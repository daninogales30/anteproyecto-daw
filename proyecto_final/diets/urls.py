from django.urls import path

from diets import views

app_name = 'diets'

urlpatterns = [
    path("", views.DietTemplateView.as_view(), name="index"),
    path("create_semanaldiet/", views.SemanalDietFormView.as_view(), name="form_semanaldiet"),
    path("list_semanaldiets/", views.PersonDietListView.as_view(), name="list_semanaldiets"),
    path("<int:pk>/delete/", views.PersonDietDeleteView.as_view(), name="person_delete_semanaldiet"),
]