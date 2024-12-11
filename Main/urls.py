from django.urls import path
from . import views

urlpatterns = [
    path('', views.client, name='client'),
    path('admin/', views.admin, name='admin'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('mechanic_slot/', views.mechanic_slot, name='mechanic_slots'),
]