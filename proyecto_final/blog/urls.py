from django.urls import path

from blog.views import EntradaListView, EntradaFormView, BlogTemplateView

app_name = 'blog'

urlpatterns = [
    path('', BlogTemplateView.as_view(), name='index'),
    path('index/', EntradaListView.as_view(), name='list'),
    path('create_entry/', EntradaFormView.as_view(), name='create_entry'),
]