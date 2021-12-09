from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',LoginView.as_view(),name="login"),
    path('logout',LogoutView.as_view(),name='logout'),
    path('register',csrf_exempt(RegisterView.as_view()),name="register"),
    path('dashboard',DashboardView.as_view(),name="dashboad")
]