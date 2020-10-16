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
                            X=row['X'],
                            Y=row['Y'],
                            Unique_Squirrel_ID=row['Unique Squirrel ID'],
                            Shift=row['Shift'],
                            Date=row['Date'],
                            Age=row['Age'],
                            PrimaryFurColor=row['Primary Fur Color'],
                            Location=row['Location'],
                            SpecificLocation=row['Specific Location'],
                            Running=strtobool(row['Running']),
                            Chasing=strtobool(row['Chasing']),
                            Climbing=strtobool(row['Climbing']),
                            Eating=strtobool(row['Eating']),
                            Foraging=strtobool(row['Foraging']),
                            OtherActivities=row['Other Activities'],
                            Kuks=strtobool(row['Kuks']),
                            Quaas=strtobool(row['Quaas']),
                            Moans=strtobool(row['Moans']),
                            TailFlags=strtobool(row['Tail flags']),
                            TailTwitches=strtobool(row['Tail twitches']),
                            Approaches=strtobool(row['Approaches']),
                            Indifferent=strtobool(row['Indifferent']),
                            RunsFrom=strtobool(row['Runs from']),
                    )
            path = kwargs['path']
            with open(path, 'rt') as f:
                reader = csv.reader(f, dialect='excel')
                next(reader,None)
                try:
                    for row in reader:
                        squirrel = Squirrel.objects.create(
                        X=row[0],
                        Y=row[1],
                        Unique_Squirrel_ID=row[2],
                        Shift=row[4],
                        Date = str(row[5])[4:] + '-' + str(row[5])[:2] + '-' + str(row[5])[2:4],
                        Age=row[7],
                        PrimaryFurColor=row[8],
                        Location=row[12],
                        SpecificLocation=row[14],
                        Running=(row[15]=='true'),
                        Chasing=(row[16]=='true'),
                        Climbing=(row[17]=='true'),
                        Eating=(row[18]=='true'),
                        Foraging=(row[19]=='true'),
                        OtherActivities=row[20],
                        Kuks=(row[21]=='true'),
                        Quaas=(row[22]=='true'),
                        Moans=(row[23]=='true'),
                        TailFlags=(row[24]=='true'),
                        TailTwitches=(row[25]=='true'),
                        Approaches=(row[26]=='true'),
                        Indifferent=(row[27]=='true'),
                        RunsFrom=(row[28] == 'true'),
                        )
                    squirrel.save()
                except:
                    pass
                msg = f'You are importing'
                self.stdout.write(self.style.SUCCESS(msg))

