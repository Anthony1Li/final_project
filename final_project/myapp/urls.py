from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('map/', views.map, name = 'map'),
    path('sightings/', views.sightings, name = 'sightings'),
    path('sightings/<str:unque_squirrel_id>', views.edit, name = 'edit'),
    path('sightings/add', views.add, name = 'add'),
    path('sightings/stat', views.stat, name = 'stat'),
]