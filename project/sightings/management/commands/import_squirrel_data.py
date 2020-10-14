import csv

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Get squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('rows.csv', help = 'file containing squirrel details')

    def handle(self, *args, **options):
        file_ = options['rows.csv']
