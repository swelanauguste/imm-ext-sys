import csv

from django.core.management.base import BaseCommand

from ...models import PortOfEntry


class Command(BaseCommand):
    help = "Import data from a CSV file"

    # def add_arguments(self, parser):
    #     parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        # csv_file = kwargs['csv_file']
        with open(f"static/docs/ports_of_entry_list.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, code, entry_type = row
                port, created = PortOfEntry.objects.get_or_create(
                    name=name, code=code, entry_type=entry_type
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Created PortOfEntry: {name}")
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f"PortOfEntry already exists: {name}")
                    )
