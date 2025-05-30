from django.urls import path

from blog.views import EntradaListView, EntradaFormView, BlogTemplateView, EntradaDeleteView, EntradaUpdateView

app_name = 'blog'

urlpatterns = [
    path('', BlogTemplateView.as_view(), name='index'),
    path('index/', EntradaListView.as_view(), name='list'),
    path('create_entry/', EntradaFormView.as_view(), name='create_entry'),
    path('<int:pk>/update/', EntradaUpdateView.as_view(), name='edit_entry'),
    path('<int:pk>/delete/', EntradaDeleteView.as_view(), name='delete_entry'),
]