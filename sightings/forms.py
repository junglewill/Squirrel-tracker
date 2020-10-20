from django.forms import ModelForm

from .models import Squirrel


class AddNewForm(ModelForm):
    class Meta:
        model = Squirrel
        # All other fields are handled in the background
        fields = [
                             'X', 
                             'Y', 
                             'Unique Squirrel ID', 
                             'Shift', 
                             'Date', 
                             'Age', 
                             'Primary Fur Color', 
                             'Location', 
                             'Specific Location', 
                             'Running', 
                             'Chasing', 
                             'Climbing', 
                             'Eating', 
                             'Foraging', 
                             'Other Activities', 
                             'Kuks', 
                             'Quaas', 
                             'Moans', 
                             'Tail Flags', 
                             'Tail Twitches', 
                             'Approaches', 
                             'Indifferent', 
                             'Runs From',
        ]
