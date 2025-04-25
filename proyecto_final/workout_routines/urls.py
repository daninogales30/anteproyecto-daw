from django.urls import path
from workout_routines import views

app_name = 'workout_routines'

urlpatterns = [
    path('create_routine/', views.RoutineFormView.as_view(), name='form_routine'),
    path('create_workout/', views.WorkoutFormView.as_view(), name='form_workout'),
    path('workout/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout_detail'),
    path('workout_preloaded', views.PreloadedWorkoutsListView.as_view(), name='workout_preloaded'),
    path('workout/<int:pk>/routine_delete', views.RoutineDeleteView.as_view(), name='routine_delete'),
    path('workout/<int:pk>/delete', views.WorkoutDeleteView.as_view(), name='workout_delete'),
]