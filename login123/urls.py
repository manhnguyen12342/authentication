from django.urls import path
from login123.views import registerviews,LoginViews
urlpatterns = [
    path('register', registerviews.as_view(),),
    path('login', LoginViews.as_view()),
]
