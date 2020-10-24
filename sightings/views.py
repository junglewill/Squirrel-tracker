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

def squirrel_details(request, Unique_Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, pk=Unique_Squirrel_ID)

    context = {
        'squirrel': squirrel,
    }
    return render(request, 'sightings/detail.html', context)

def request_a_pet(request):
    obj = Squirrel()
    obj.Latitude = 'This is the title'
    obj.Longitude = 'This is the content'
    obj.Unique_Squirrel_ID
    obj.Shift
    obj.Date
    obj.Age
    obj.Primary_Fur_Color
obj.Location
obj.Specific_Location
obj.Running
obj.Chasing
obj.Climbing
obj.Eating
obj.Foraging
obj.Other_Activities
obj.Kuks
obj.Quaas
obj.Moans
obj.Tail_Flags
obj.Tail_Twitches
obj.Approaches
obj.Indifferent
obj.Runs_From
    article.save()
    if request.method == 'POST':
        form = AdoptRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({})

# Create your views here.
