from django.urls import path, re_path
  
from . import views
app_name = 'sightings'
urlpatterns = [
        path('', views.index, name='index'),
        re_path(r'^sightings/(?P<Unique_Squirrel_ID>[0-9A-Z -]+)/$', views.squirrel_details, name='details'),
]
