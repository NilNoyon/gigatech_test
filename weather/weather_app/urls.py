from django.urls import path
from . import views

# BUILDER'S SECTION
urlpatterns = [
    path('', views.index, name='index'),
]