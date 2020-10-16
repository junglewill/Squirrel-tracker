from django.urls import path
  
from . import views
app_name = 'sightings'
urlpatterns = [
        path('', views.index),
        #path('<intunique_squirrel_id>/', views.detail, name='detail'),
]
