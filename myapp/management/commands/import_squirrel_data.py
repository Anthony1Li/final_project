from django.core.management import BaseCommand
from myapp.models import squirrel_data
import csv

class Command(BaseCommand):
    help = 'import data'

    def add_arguments(self, parser):
        parser.add_argument('path',type=str,help="csv file")

    def handle(self, path, **options):
        with open(path, 'r',encoding='UTF-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                _, created = squirrel_data.objects.get_or_create(
                    latitude = row[0],
                    longitude= row[1],
                    unique_squirrel_id = row[2],
                    shift = row[4],
                    date = row[5][4:8]+'-'+ row[5][0:2]+'-'+ row[5][2:4],
                    age = row[7],
                    primary_fur_color = row[8],
                    location = row[12],
                    specific_location = row[14],
                    running = True if row[15].lower()=='true' else False,
                    chasing = True if row[16].lower()=='true' else False,
                    climbing = True if row[17].lower()=='true' else False,
                    eating = True if row[18].lower()=='true' else False,
                    foraging = True if row[19].lower()=='true' else False,
                    other_activities = row[20],
                    kuks = True if row[21].lower()=='true' else False,
                    quaas = True if row[22].lower()=='true' else False,
                    moans = True if row[23].lower()=='true' else False,
                    tail_flags = True if row[24].lower()=='true' else False,
                    tail_twitches = True if row[25].lower()=='true' else False,
                    approaches = True if row[26].lower()=='true' else False,
                    indifferent = True if row[27].lower()=='true' else False,
                    runs_from = True if row[28].lower()=='true' else False,)