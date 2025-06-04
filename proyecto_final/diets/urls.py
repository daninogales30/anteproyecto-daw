from django.urls import path

from diets import views

app_name = 'diets'

urlpatterns = [
    path("", views.DietTemplateView.as_view(), name="index"),
    path("create_semanaldiet/", views.SemanalDietFormView.as_view(), name="form_semanaldiet"),
    path("create_fooditem/", views.FoodItemFormView.as_view(), name="form_fooditem"),
    path("list_semanaldiets/", views.PersonDietListView.as_view(), name="list_semanaldiets"),
    path("list_semanaldiets_precharged/", views.TodasDietasPrecargadasListView.as_view(),
         name="list_semanaldiets_precharged"),
    path("list_semanaldiets_precharged/<int:pk>/details/", views.DietasPrecargadasDetailView.as_view(),
         name="details_semanaldiet_precharged"),
    path("<int:pk>/update/", views.PersonSemanalDietUpdateView.as_view(), name="update_semanaldiet"),
    path("<int:pk>/details/", views.PersonDietDetailView.as_view(), name="details_semanaldiet"),
    path("<int:pk>/delete/", views.PersonDietDeleteView.as_view(), name="person_delete_semanaldiet"),
    path("daydiet/<int:pk>/delete/", views.PersonDayDietDeleteView.as_view(), name="person_delete_daydiet"),
    path("daydiet/<int:pk>/update/", views.PersonDayDietUpdateView.as_view(), name="person_update_daydiet"),
    path("create_daydiet/", views.DayDietFormView.as_view(), name="form_daydiet"),
    path("create_day/", views.DayFormView.as_view(), name="form_day"),
    path('ajax/load-days/', views.LoadDaysView.as_view(), name='ajax_load_days'),
]
