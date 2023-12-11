from django.urls import path
from . import views

urlpatterns = [
    path('', views.musicians_list, name='musicians_list'),
    path('add/', views.add_musician, name='add_musician'),
    path('edit_musician/<int:pk>/', views.edit_musician, name='edit_musician'),
    path('musician_detail/<int:pk>/', views.musician_detail, name='musician_detail'),
    path('<int:musician_id>/delete/', views.delete_musician, name='delete_musician'),
]
