from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogTemplateView.as_view(), name='index'),
    path('index/', views.EntradaListView.as_view(), name='list'),
    path('create_entry/', views.EntradaFormView.as_view(), name='create_entry'),
    path('top_bloggers/', views.TopBloggersListTemplateView.as_view(), name='top_bloggers'),
    path('api/top_bloggers/', views.TopBloggersList.as_view(), name='api_top_bloggers'),
    path('<int:pk>/update/', views.EntradaUpdateView.as_view(), name='edit_entry'),
    path('<int:pk>/delete/', views.EntradaDeleteView.as_view(), name='delete_entry'),
]
