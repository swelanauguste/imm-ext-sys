from datetime import datetime, timedelta
from random import choice, randint

from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User

from ...models import Enquiry, MaritalStatus, PortOfEntry


class Command(BaseCommand):
    help = "Generate fake enquiries"

    def handle(self, *args, **kwargs):
        fake = Faker()
        marital_statuses = MaritalStatus.objects.all()
        ports_of_entry = PortOfEntry.objects.all()

        PURPOSE_CHOICES = [
            ("Tourism", "Tourism"),
            ("Business", "Business"),
            ("Education", "Education"),
            ("Medical Treatment", "Medical Treatment"),
            ("Family Visit", "Family Visit"),
            ("Other", "Other"),
        ]

        MEANS_OF_SUPPORT_CHOICES = [
            ("Personal Savings", "Personal Savings"),
            ("Sponsorship", "Sponsorship"),
            ("Employment", "Employment"),
            ("Other", "Other"),
        ]

        for _ in range(20):
            arrived_via_options = ["Last stop off", "Straight flight"]
            purpose_of_visit, _ = choice(PURPOSE_CHOICES)
            means_of_support, _ = choice(MEANS_OF_SUPPORT_CHOICES)
            tempt_res = choice([True, False])
            perm_res = choice([True, False])
            days_difference = randint(14, 180)
            time_granted_from = fake.past_date(start_date="-5y")
            time_granted_to = time_granted_from + timedelta(days=days_difference)
            enquiry = Enquiry(
                surname=fake.last_name(),
                christian_names=fake.first_name(),
                pob=fake.city(),
                dob=fake.date_of_birth(minimum_age=18, maximum_age=100),
                nationality=fake.country(),
                foreign_address=fake.address(),
                foreign_address1=fake.address(),
                phone=fake.phone_number(),
                email=fake.email(),
                occu=fake.job(),
                marital_status=choice(marital_statuses),
                ppn=fake.uuid4()[:6],
                pp_exp=fake.future_date(end_date="+10y"),
                pp_issue_place=fake.city(),
                pp_issue_date=fake.past_date(start_date="-10y"),
                arrival_date=fake.date_this_year(),
                arrival_place=choice(ports_of_entry),
                arrived_from=fake.country(),
                arrived_via=choice(arrived_via_options),
                pov=purpose_of_visit,
                host_id_no=fake.uuid4()[:6],
                imm_offr=User.objects.get(pk=1),
                time_granted_from=fake.past_date(start_date="-5y"),
                time_granted_to=time_granted_from + timedelta(days=days_difference),
                time_granted=days_difference,
                tempt_res=tempt_res,
                perm_res=perm_res,
                address_in_st_lucia=fake.address(),
                tel_in_st_lucia=fake.phone_number(),
                means_of_support=means_of_support,
                ticket_no=fake.uuid4()[:6],
                validity=fake.date_between(start_date="today", end_date="+6m"),
            )
            enquiry.marital_status = choice(marital_statuses)
            enquiry.arrival_place = choice(ports_of_entry)
            enquiry.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Created Enquiry: {enquiry.surname.title()} {enquiry.christian_names.title()} - {enquiry.ppn.upper()}"
                )
            )
