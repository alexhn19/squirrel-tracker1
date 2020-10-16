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
                dict_['Unique Squirrel ID'] = item.unique_squirrel_ID
                dict_['Shift'] = item.Shift
                dict_['Date'] = item.Date 
                dict_['Age'] = item.Age
                dict_['Primary Fur Color'] = item.Primary_Fur_Color
                dict_['Location'] = item.Location
                dict_['Specific Location'] = item.Specific_Location 
                dict_['Running'] = item.Running
                dict_['Chasing'] = item.Chasing
                dict_['Climbing'] = item.Climbing
                dict_['Eating'] = item.Eating
                dict_['Foraging'] = item.Foraging
                dict_['Other Activities'] = item.Other_Activities 
                dict_['Kuks'] = item.Kuks
                dict_['Quaas'] = item.Quaas
                dict_['Moans'] = item.Moans
                dict_['Tail flags'] = item.Tail_Flags
                dict_['Tail twitches'] = item.Tail_Twitches
                dict_['Approaches'] = item.Approaches 
                dict_['Indifferent'] = item.Indifferent
                dict_['Runs from'] = item.Runs_From
                
                write = csv.DictWRiter(fp, delimter = ",", fieldnames = dict_.keys())
                write.writeheader()
                write.writerow(dict_)
            msg = f'You are exporting to {file_}'
            self.stdout.write(self.style.SUCCESS(msg))
