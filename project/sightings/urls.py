from django.urls import path

from . import views


urlpatterns = [
        path('', views.index),
        path('sightings/add/',views.add_squirrel),
        path('sightings/stats/',views.get_stats),
        path('sightings/<str:unique_squirrel_id>/',views.update_squirrel),
        path('sightings/',views.sighting),
        path('map/',views.map),
        ]
