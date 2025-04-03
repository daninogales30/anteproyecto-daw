from django.urls import path
from workout_routines import views

app_name = 'workout_routines'

urlpatterns = [
    path('create_workout/', views.WorkoutFormView.as_view(), name='form_workout'),
    path('create_routine/', views.RoutineFormView.as_view(), name='form_routine'),
    path('list/', views.RoutineListView.as_view(), name='list'),
]
