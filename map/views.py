from django.shortcuts import render
from sightings.models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }

    return render(request, "map/index.html", {})
# Create your views here.
