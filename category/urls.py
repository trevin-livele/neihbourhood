from django.urls import path,include
from .import views

urlpatterns = [
    path('category/',views.cat, name='cat'),


]
