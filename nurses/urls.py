from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add/', views.add_nurse, name='add_nurse'),

    path('edit/<int:id>/', views.edit_nurse, name='edit_nurse'),

    path('delete/<int:id>/', views.delete_nurse, name='delete_nurse'),
]