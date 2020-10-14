import csv

from django.core.management.base import BaseCommand

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Export squirrel data'
  
    def add_arguments(self, parser):
        parser.add_argument('squirrel.csv', help = 'create file containing squirrel data')
    def handle(self, *args, **options):
        file_ = options['squirrel.csv']
        with open(file_, 'w') as fp:
            s = Squirrel.objects.all()
            for item in s:
                obj = Squirrel()
                item['X'] = obj.latitude
                item['Y'] = obj.longitude
                item['Unique Squirrel ID'] = obj.unique_squirrel_id
                item['Shift'] = obj.shift
                item['Date'] = obj.date 
                item['age'] = obj.age
                item['Primary Fur Color'] = obj.primary_fur_color
                item['Location'] = obj.location
                item['Specific Location'] = obj.specific_location 
                item['Running'] = obj.running
                item['Chasing'] = obj.chasing
                item['Climbing'] = obj.climbing
                item['Eating'] = obj.eating
                item['Foraging'] = obj.foraging
                item['Other Activities'] = obj.other_activities 
                item['Kuks'] = obj.kuks
                item['Quaas'] = obj.quaas
                item['Moans'] = obj.moans
                item['Tail flags'] = obj.tail_flags
                item['Tail twitches'] = obj.tail_twitches
                item['Approaches'] = obj.approaches 
                item['Indifferent'] = obj.indifferent
                item['Runs from'] = obj.runs_from
                obj.save()
            msg = f'You are exporting to {file_}'
            self.stdout.write(self.style.SUCCESS(msg))
