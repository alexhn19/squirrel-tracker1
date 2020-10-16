from django.urls import path

from . import views


urlpatterns = [
        path('', views.index),
        path('sightings/add/',views.add_squirrel),
        path('sightings/stats/',views.get_stats),
        path('sightings/<str:Unique_Squirrel_ID>/',views.update_squirrel),
        path('sightings/',views.sighting),
        path('map/',views.map),
        ]
