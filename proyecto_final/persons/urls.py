from django.urls import path

from persons import views

app_name = 'persons'

urlpatterns = [
    path('register/', views.PersonRegisterCreateView.as_view(), name='register'),
    path('', views.PersonLoginView.as_view(), name='login'),
    path('index/', views.PersonIndexView.as_view(), name='index'),
    path('profile/', views.PersonDetailView.as_view(), name='profile'),
    path('update/', views.PersonUpdateView.as_view(), name='update'),
    path('update-password/', views.PersonPasswordUpdateView.as_view(), name='password'),
]
