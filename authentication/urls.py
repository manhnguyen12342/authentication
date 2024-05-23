from django.urls import path
from authentication.views import (
    Registerview,
    LoginView,
    LogoutView,
    # CreateWeatherData,
    # GetDataDetail,
    # UpdateWeatherData,
    # DeleteWeatherData
)
urlpatterns = [
    path('register', Registerview.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    # path('create',CreateWeatherData.as_view()),
    # path('get',GetDataDetail.as_view()),
    # path('update',UpdateWeatherData.as_view()),
    # path('delete',DeleteWeatherData.as_view()),
]
