from django.urls import path
from .views import search_view, search_results_view

app_name = 'search'

urlpatterns = [
    path('', search_view, name='search'),
    path('results/', search_results_view, name='search_results'),
]