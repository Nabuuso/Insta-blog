from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('',LoginView.as_view(),name="login"),
    path('register',csrf_exempt(RegisterView.as_view()),name="register")
]