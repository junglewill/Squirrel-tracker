from django.urls import path
  
from . import views
app_name = 'sightings'
urlpatterns = [
        path('', views.index, name='index'),
        path('<int:Unique_Squirrel_ID>/', views.squirrel_details, name='details'),
]
