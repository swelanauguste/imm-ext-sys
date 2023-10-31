import csv
from django.core.management.base import BaseCommand
from ...models import PaymentType

class Command(BaseCommand):
    help = 'Import payment types from a CSV file'

    def handle(self, *args, **kwargs):
        csv_file = "static/docs/payment_type_list.csv"  # Hardcoded file path

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    name, desc = [value.strip() for value in row]
                    payment_type, created = PaymentType.objects.get_or_create(
                        name=name,
                        desc=desc
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Created PaymentType: {name}'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'PaymentType already exists: {name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Invalid line format: {row}'))
