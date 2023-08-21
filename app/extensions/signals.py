from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    Enquiry,
    EnquiryPayment,
    IndividualArrears,
    SubsequentPermit,
    SubsequentPermitPayment,
)


@receiver(post_save, sender=Enquiry)
def create_individual_arrears(sender, instance, created, **kwargs):
    if created:
        IndividualArrears.objects.create(enquiry=instance)


# @receiver(post_save, sender=Enquiry)
# def save_individual_arrears(sender, instance, **kwargs):
#     instance.enquiry_arrears.save()


@receiver(post_save, sender=Enquiry)
def create_enquiry_payment(sender, instance, created, **kwargs):
    if created:
        EnquiryPayment.objects.create(enquiry=instance)


# @receiver(post_save, sender=Enquiry)
# def save_enquiry_payment(sender, instance, **kwargs):
#     instance.enquiry.save()


@receiver(post_save, sender=SubsequentPermit)
def create_subsequent_permit_payment(sender, instance, created, **kwargs):
    if created:
        SubsequentPermitPayment.objects.create(subsequent_permit=instance)


# @receiver(post_save, sender=SubsequentPermit)
# def save_subsequent_permit_payment(sender, instance, **kwargs):
#     instance.subsequent_permit.save()
