from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('ordens/', views.ordens, name='ordens'),
    path('members/', views.members, name='members'),
    path('members/detalhes/<int:id>', views.details, name='detalhes'),
    path('testing/', views.testing, name='testing'),  
]