import csv

from django.core.management import BaseCommand
from sightings.models import Squirrel
import argparse

from distutils.util import strtobool

class Command(BaseCommand):
        help = 'Load squirrel data  into the database'
            
        def add_arguments(self,parser):
            parser.add_argument('path', type=str)

        def handle(self, *args, **kwargs):
            Squirrel.objects.all().delete()
            path = kwargs['path']
            with open(path, 'rt') as f:
                reader = csv.DictReader(f)
                data = list(reader)
                for row in data:
                    squirrel = Squirrel(
                            latitude=row['X'],
                            longitude=row['Y'],
                            unique_squirrel_id=row['Unique Squirrel ID'],
                            shift=row['Shift'],
                            date=row['Date'],
                            age=row['Age'],
                            primary_fur_color=row['Primary Fur Color'],
                            location=row['Location'],
                            specific_location=row['Specific Location'],
                            running=strtobool(row['Running']),
                            chasing=strtobool(row['Chasing']),
                            climbing=strtobool(row['Climbing']),
                            eating=strtobool(row['Eating']),
                            foraging=strtobool(row['Foraging']),
                            other_Activities=row['Other Activities'],
                            kuks=strtobool(row['Kuks']),
                            quaas=strtobool(row['Quaas']),
                            moans=strtobool(row['Moans']),
                            tail_flags=strtobool(row['Tail flags']),
                            tail_twitches=strtobool(row['Tail twitches']),
                            approaches=strtobool(row['Approaches']),
                            indifferent=strtobool(row['Indifferent']),
                            runs_from=strtobool(row['Runs from']),
                    )
            path = kwargs['path']
            with open(path, 'rt') as f:
                reader = csv.reader(f, dialect='excel')
                next(reader,None)
                try:
                    for row in reader:
                        squirrel = Squirrel.objects.create(
                        latitude=row[0],
                        longitude=row[1],
                        unique_squirrel_id=row[2],
                        shift=row[4],
                        date = str(row[5])[4:] + '-' + str(row[5])[:2] + '-' + str(row[5])[2:4],
                        age=row[7],
                        primary_fur_color=row[8],
                        location=row[12],
                        specific_location=row[14],
                        running=(row[15]=='true'),
                        chasing=(row[16]=='true'),
                        climbing=(row[17]=='true'),
                        eating=(row[18]=='true'),
                        foraging=(row[19]=='true'),
                        other_activities=row[20],
                        kuks=(row[21]=='true'),
                        quaas=(row[22]=='true'),
                        moans=(row[23]=='true'),
                        tail_flags=(row[24]=='true'),
                        tail_twitches=(row[25]=='true'),
                        approaches=(row[26]=='true'),
                        indifferent=(row[27]=='true'),
                        runs_from=(row[28] == 'true'),
                        )
                    squirrel.save()
                except:
                    pass
                msg = f'You are importing'
                self.stdout.write(self.style.SUCCESS(msg))

