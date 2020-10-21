import csv
  
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
                                                          
class Command(BaseCommand):                                                         
    help = ("Exporting data to .csv")
                                                          
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=open)
                                                          
    def handle(self, *args, **options):
        field_list = [f.name for f in Squirrel._meta.get_fields()]                     
        with open('csv_file', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_list)
                                                          
            for obj in Squirrel.objects.all():
                value_list = []
                for f in field_list:
                    value = getattr(obj, f)
                    value_list.append(value)
                writer.writerow(value_list)
            csvfile.close()
