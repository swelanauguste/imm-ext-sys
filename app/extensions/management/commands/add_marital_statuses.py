from django.core.management.base import BaseCommand
from ...models import MaritalStatus

class Command(BaseCommand):
    help = 'Add hardcoded marital statuses'

    def handle(self, *args, **kwargs):
        marital_statuses = [
            {"name": "Single"},
            {"name": "Married"},
            {"name": "Divorced"},
            {"name": "Widowed"},
            # Add more marital statuses as needed
        ]

        for status_data in marital_statuses:
            name = status_data["name"]

            status, created = MaritalStatus.objects.get_or_create(
                name=name
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created MaritalStatus: {name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'MaritalStatus already exists: {name}'))
