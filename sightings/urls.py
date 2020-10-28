from django.urls import path, re_path
  
from . import views
app_name = 'sightings'
urlpatterns = [
        path('', views.index, name='index'),
        re_path(r'^(?P<Unique_Squirrel_ID>[0-9A-Za-z -]+)/$', views.squirrel_details, name='details'),
        path('add/', views.add, name='add'),
        path('request/', views.add_squirrel, name='request'),
        ]
