from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel

import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('/home/pl2775/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['/home/pl2775/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            for row in dataReader:
                squirrel = Squirrel()
                squirrel.x = row[0]
                squirrel.y = row[1]
                squirrel.unique_squirrel_id = row[2]
                squirrel.hectare = row[3]
                squirrel.shift = row[4]
                squirrel.date = row[5]
                squirrel.hectare_squirrel_number = row[6]
                squirrel.age = row[7]
                squirrel.primary_fur_color = row[8]
                squirrel.highlight_fur_color = row[9]
                squirrel.combination_of_primary_and_highlight_color = row[10]
                squirrel.color_notes = row[11]
                squirrel.location = row[12]
                squirrel.above_ground_sighter_measurement = row[13]
                squirrel.specific_location = row[14]
                squirrel.running = row[15]
                squirrel.chasing = row[16]
                squirrel.climbing = row[17]
                squirrel.eating = row[18]
                squirrel.foraging = row[19]
                squirrel.other_activities = row[20]
                squirrel.kuks = row[21]
                squirrel.quaas = row[22]
                squirrel.moans = row[23]
                squirrel.tail_flags = row[24]
                squirrel.tail_twitches = row[25]
                squirrel.approaches = row[26]
                squirrel.indifferent = row[27]
                squirrel.runs_from = row[28]
                squirrel.other_interactions = row[29]
                squirrel.lat_long = row[30]
            msg = 'You are importing data...'    
            self.stdout.write(
                    self.style.SUCCESS(msg)
                )
