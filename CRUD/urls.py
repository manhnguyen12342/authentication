from django.urls import path
from CRUD.views import (
    WeatherDataListCreateView,
    WeatherDataDetailView,
    WeatherDataUpdateView,
    WeatherDataDeleteView
)
urlpatterns = [
    path('create',WeatherDataListCreateView.as_view()),
    path('get',WeatherDataDetailView.as_view()),
    path('update/<int:id>',WeatherDataUpdateView.as_view()),
    path('delete/<int:id>',WeatherDataDeleteView.as_view()),
]
