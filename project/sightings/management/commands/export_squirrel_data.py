import csv

from django.core.management.base import BaseCommand

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Export squirrel data'
  
    def add_arguments(self, parser):
        parser.add_argument('csv_file', help = 'create file containing squirrel data')
    def handle(self, *args, **options):
        dict_ = {}
        s = Squirrel.objects.all()
        with open(options['csv_file'], 'w') as fp:
            for item in s:
                dict_['X'] = item.X
                dict_['Y'] = item.Y
                dict_['Unique Squirrel ID'] = item.unique_squirrel_id
                dict_['Shift'] = item.shift
                dict_['Date'] = item.date 
                dict_['Age'] = item.age
                dict_['Primary Fur Color'] = item.primary_fur_color
                dict_['Location'] = item.location
                dict_['Specific Location'] = item.specific_location 
                dict_['Running'] = item.running
                dict_['Chasing'] = item.chasing
                dict_['Climbing'] = item.climbing
                dict_['Eating'] = item.eating
                dict_['Foraging'] = item.foraging
                dict_['Other Activities'] = item.other_activities 
                dict_['Kuks'] = item.kuks
                dict_['Quaas'] = item.quaas
                dict_['Moans'] = item.moans
                dict_['Tail flags'] = item.tail_flags
                dict_['Tail twitches'] = item.tail_twitches
                dict_['Approaches'] = item.approaches 
                dict_['Indifferent'] = item.indifferent
                dict_['Runs from'] = item.runs_from
                
                write = csv.DictWriter(fp, delimiter = ",", fieldnames = dict_.keys())
                write.writeheader()
                write.writerow(dict_)
            msg = f'You are exporting'
            self.stdout.write(self.style.SUCCESS(msg))
