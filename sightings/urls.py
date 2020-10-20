from django.urls import path
  
from . import views
app_name = 'sightings'
urlpatterns = [
        path('', views.index),
        path('<int:Unique_Squirrel_ID>/', views.detail, name='detail'),
]
