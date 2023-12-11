from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_album, name="add_album"),
    path('album_detail/<int:album_id>/', views.album_detail, name='album_detail'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
]
