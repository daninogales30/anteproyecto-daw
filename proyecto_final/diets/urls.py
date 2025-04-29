from django.urls import path

from diets import views

app_name = 'diets'

urlpatterns = [
    path("", views.DietTemplateView.as_view(), name="index"),
    path("create_semanaldiet/", views.SemanalDietFormView.as_view(), name="form_semanaldiet"),
    path("create_fooditem/", views.FoodItemFormView.as_view(), name="form_fooditem"),
    path("list_semanaldiets/", views.PersonDietListView.as_view(), name="list_semanaldiets"),
    path("<int:pk>/details", views.PersonDietDetailView.as_view(), name="details_semanaldiet"),
    path("<int:pk>/delete/", views.PersonDietDeleteView.as_view(), name="person_delete_semanaldiet"),
]