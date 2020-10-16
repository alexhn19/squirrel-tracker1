import csv

from django.core.management.base import BaseCommand

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Load squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help = 'file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['csv_file']
        
        try:

            with open(file_) as fp:
                reader = csv.DictReader(fp)


                for item in reader:
                    obj = Squirrel()

                    obj.latitude = item['X']
                    obj.longitude = item['Y']
                    obj.unique_squirrel_id = item['Unique Squirrel ID']
                    obj.hectare = item['Hectare']
                    obj.shift = item['Shift']
                    obj.date = item['Date']
                    obj.age = item['Age']
                    obj.primary_fur_color = item['Primary Fur Color']
                    obj.location = item['Location']
                    obj.specific_location = item['Specific Location']
                    obj.running = item['Running']
                    obj.chasing = item['Chasing']
                    obj.climbing = item['Climbing']
                    obj.eating = item['Eating']
                    obj.foraging = item['Foraging']
                    obj.other_activities = item['Other Activities']
                    obj.kuks = item['Kuks']
                    obj.quaas = item['Quaas']
                    obj.moans = item['Moans']
                    obj.tail_flags = item['Tail flags']
                    obj.tail_twitches = item['Tail twitches']
                    obj.approaches = item['Approaches']
                    obj.indifferent = item['Indifferent']
                    obj.runs_from = item['Runs from']

                    obj.save()

                msg = f'You are importing from {file_}'

                self.stdout.write(self.style.SUCCESS(msg))
        except csv.Error as e:
                print(f'there is something wrong with {fp.line_num}')

