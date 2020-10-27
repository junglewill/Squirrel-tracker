from django.http import JsonResponse
from django.shortcuts import render
from sightings.models import Squirrel
from sightings.forms import AddNewForm

from django.shortcuts import get_object_or_404

def index(request):
    squirrels = Squirrel.objects.all()

    context = {
            'squirrels': squirrels,
            }
    field_list = [field.name for field in Squirrel._meta.get_fields()]
    return render(request, "sightings/index.html", context)

def squirrel_details(request, Unique_Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, pk=Unique_Squirrel_ID)

    context = {
        'squirrel': squirrel,
    }
    return render(request, 'sightings/detail.html', context)

def add_squirrel(request):

    if request.method == 'POST':
        form = AddNewForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({})

# Create your views here.
