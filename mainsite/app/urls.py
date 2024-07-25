from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard , name="dashboard"),
    path('delete/<int:pk>', views.delete_items, name="delete"),
    path('exceeds/',views.exceeds_view, name = 'exceeds'),
]