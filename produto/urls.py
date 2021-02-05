from django.urls import path
from produto import views

urlpatterns = [
    path('home/', views.home, name = "home")
]
