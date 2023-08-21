from django.db import models
from users.models import User
from django.shortcuts import reverse

class PortOfEntry(models.Model):
    ENTRY_TYPE_CHOICES = (
        ("AIR", "AIR"),
        ("SEA", "SEA"),
    )
    name = models.CharField(max_length=255)
    entry_type = models.CharField(
        max_length=3, choices=ENTRY_TYPE_CHOICES, default=ENTRY_TYPE_CHOICES[0][0]
    )

    def __str__(self):
        return self.name


class MaritalStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    img = models.ImageField(upload_to="enquiry_images", blank=True, null=True)
    surname = models.CharField(max_length=255)
    christian_names = models.CharField(max_length=255)
    pob = models.CharField(max_length=255, verbose_name="place of birth")
    dob = models.DateField(verbose_name="date of birth")
    nationality = models.CharField(max_length=255)
    foreign_address = models.CharField(max_length=255)
    foreign_address1 = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    occu = models.CharField(max_length=255, verbose_name="occupation")
    marital_status = models.ForeignKey(
        MaritalStatus, on_delete=models.PROTECT, related_name="marital_statuses"
    )
    ppn = models.CharField(max_length=255, verbose_name="passport number")
    pp_exp = models.DateField(verbose_name="passport expiry date")
    pp_issue_place = models.CharField(
        max_length=255, verbose_name="passport place issued"
    )
    pp_issue_date = models.DateField(verbose_name="passport issued date")
    arrival_date = models.DateField()
    arrival_place = models.ForeignKey(
        PortOfEntry, on_delete=models.PROTECT, related_name="ports_of_entry", help_text='Air/Sea Port'
    )
    arrived_from = models.CharField(max_length=255)
    arrived_via = models.CharField(max_length=255, help_text='Straight flight/Last stop off')
    pov = models.CharField(max_length=255, verbose_name="purpose of visit")
    imm_offr = models.CharField(max_length=255, verbose_name="immigration officer")
    time_granted_from = models.DateField(verbose_name="from")
    time_granted_to = models.DateField(verbose_name="to")
    time_granted = models.CharField(max_length=255)
    address_in_st_lucia = models.CharField(
        max_length=255, verbose_name="Address in St Lucia"
    )
    tel_in_st_lucia = models.CharField(
        max_length=255, verbose_name="Telephone in St Lucia"
    )
    means_of_support = models.CharField(max_length=255)
    ticket_no = models.CharField(max_length=255, verbose_name="ticket number")
    validity = models.DateField(verbose_name="valid until", help_text='Ticket valid until')
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="enquire_created_by",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="enquire_updated_by",
        null=True,
        blank=True,
    )
    
    class Meta:
        ordering = ["-arrival_date"]

    def get_absolute_url(self):
        return reverse("enquiry-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.surname} {self.christian_names} - {self.ppn}"


class EnquiryRemarks(models.Model):
    """
    This is the model for the remarks
    """

    enquiry = models.ForeignKey(
        Enquiry, on_delete=models.PROTECT, related_name="enquiry_remarks"
    )
    remarks = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="remarks_created_by",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="remarks_updated_by",
        null=True,
        blank=True,
    )
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.enquiry.surname} {self.enquiry.christian_names} - {self.enquiry.ppn}"


class EnquiryPayment(models.Model):
    """
    This is the model for the payment
    """

    enquiry = models.ForeignKey(
        Enquiry, on_delete=models.PROTECT, related_name="enquiry_payments"
    )
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    payment_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    payment_date = models.DateField(blank=True, null=True)
    receipt_no = models.CharField(
        max_length=255, verbose_name="receipt number", null=True, blank=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="enquiry_payment_created_by",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="enquiry_payment_updated_by",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.enquiry} - {self.receipt_no}"


class SubsequentPermit(models.Model):
    """
    This is the model for the subsequent permits
    """

    enquirie = models.ForeignKey(
        Enquiry, on_delete=models.PROTECT, related_name="enquiries"
    )
    length_of_stay = models.CharField(max_length=255, blank=True)
    time_granted = models.CharField(max_length=255)
    time_granted_from = models.DateField(verbose_name="from")
    time_granted_to = models.DateField(verbose_name="to")
    granted_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="granted_by"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="subsequent_permit_created_by",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="subsequent_permit_updated_by",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.application.surname} {self.application.christian_names} - {self.application.ppn} remarks"


class SubsequentPermitRemarks(models.Model):
    """
    This is the model for the remarks
    """

    subsequent_permit = models.ForeignKey(
        SubsequentPermit,
        on_delete=models.PROTECT,
        related_name="subsequent_permit_remarks",
    )
    remarks = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="subsequent_permit_remark_created_by",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="subsequent_permit_remark_updated_by",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.application.surname} {self.application.christian_names} - {self.application.ppn}"


class SubsequentPermitPayment(models.Model):
    """
    This is the model for the payment
    """

    subsequent_permit = models.ForeignKey(
        SubsequentPermit, on_delete=models.PROTECT, related_name="enquiry_payments"
    )
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    payment_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    payment_date = models.DateField(blank=True, null=True)
    receipt_no = models.CharField(
        max_length=255, verbose_name="receipt number", blank=True, null=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="subsequent_permit_payment_created_by",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="subsequent_permit_payment_updated_by",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.subsequent_permit} - {self.receipt_no}"


class IndividualArrears(models.Model):
    """
    This is the model for the arrears
    """

    enquiry = models.ForeignKey(
        Enquiry, on_delete=models.PROTECT, related_name="enquiry_arrears"
    )
    subsequent_permit = models.ForeignKey(
        SubsequentPermit,
        on_delete=models.PROTECT,
        related_name="subsequent_permit_arrears",
        null=True,
        blank=True,
    )

    def get_arrears_total(self):
        return f"arrears total: "

    def __str__(self):
        return f"{self.arrears.surname} {self.arrears.christian_names} - {self.arrears.ppn}"