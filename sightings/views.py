from django.shortcuts import render
from sightings.models import Squirrel

from django.shortcuts import get_object_or_404

def index(request):
    squirrels = Squirrel.objects.all()

    context = {
            'squirrels': squirrels,
            }
    field_list = [field.name for field in Squirrel._meta.get_fields()]
    return render(request, "sightings/index.html", context)

def detail(request, Unique_Squirrel_ID):

    squirrel = get_object_or_404(Squirrel, pk=Unique_Squirrel_ID)
    x = getattr(squirrel, 'Latitude')
    y = getattr(squirrel, 'Longtitude')
    unique_id = getattr(squirrel, 'Unique_Squirrel_ID')
    date = getattr(squirrel, 'Date')
    age = getattr(squirrel, 'Age')
    pf_color = getattr(squirrel, 'Primary_Fur_Color')
    context = {
            'squirrel_la': x,
            'squirrel_lo': y,
            'unique_sid': unique_id,
            'date': date,
            'age': age,
            'pf_color': pf_color,
            }
    return render(request, 'sightings/detail.index', context)

# Create your views here.
