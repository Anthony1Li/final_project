from django.urls import path

from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('map/', views.map, name = 'map'),
    path('sightings/', views.sightings, name = 'sightings'),
    path('sightings/add/', views.add, name = 'add'),
    path('sightings/stat/', views.stat, name = 'stat'),
    path('sightings/<str:unique_squirrel_id>/', views.edit, name = 'edit'),
    path('sightings/<str:unique_squirrel_id>/delete/', views.delete, name = 'delete'),
]