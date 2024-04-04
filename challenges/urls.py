from django.urls import path
from . import views

urlpatterns = [
    path("", views.month_index),
    path("<str:month>", views.monthly_challanges)
]