from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>/', views.detail_book, name='detail_book'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]