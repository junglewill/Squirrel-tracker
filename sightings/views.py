from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from sightings.models import Squirrel
from sightings.forms import AddNewForm,UpdateForm

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
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return HttpResponse('updated')
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return render(request, 'sightings/detail.html', context)

def add(request):
    if request.method == 'POST':
        form = AddNewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('You have added a new squirrel data.')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'sightings/add.html', {})

# Create your views here.
