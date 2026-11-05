from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('Home/', views.home, name='home'),
]