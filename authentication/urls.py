from django.urls import path
from authentication.views import (
    Registerview,
    LoginView,
    LogoutView,
    WeatherDataListCreateView,
    WeatherDataDetailView,
    WeatherDataUpdateView,
    WeatherDataDeleteView
)
urlpatterns = [
    path('register', Registerview.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('create',WeatherDataListCreateView.as_view()),
    path('get',WeatherDataDetailView.as_view()),
    path('update/<int:id>',WeatherDataUpdateView.as_view()),
    path('delete/<int:id>',WeatherDataDeleteView.as_view()),
]
