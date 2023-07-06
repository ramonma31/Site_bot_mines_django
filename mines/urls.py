from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('mines/', views.mines_render),
]