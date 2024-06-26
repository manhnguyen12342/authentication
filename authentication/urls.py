from django.urls import path
from authentication.views import (
    Registerview,
    LoginView,
    LogoutView,
)
urlpatterns = [
    path('register', Registerview.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
]
