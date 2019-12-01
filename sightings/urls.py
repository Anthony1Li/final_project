from django.urls import path

from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.sightings, name = 'sightings'),
    path('home/', views.home, name = 'home'),
    path('map/', views.map, name = 'map'),
    path('add/', views.add, name = 'add'),
    path('stats/', views.stats, name = 'stat'),
    path('<str:unique_squirrel_id>/', views.edit, name = 'edit'),
    path('<str:unique_squirrel_id>/delete/', views.delete, name = 'delete'),
]