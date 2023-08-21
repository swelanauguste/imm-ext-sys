from django.contrib import admin

from .models import (
    Enquiry,
    EnquiryPayment,
    EnquiryRemarks,
    IndividualArrears,
    MaritalStatus,
    PortOfEntry,
    SubsequentPermit,
    SubsequentPermitPayment,
    SubsequentPermitRemarks,
)

admin.site.register(Enquiry)
admin.site.register(EnquiryPayment)
admin.site.register(EnquiryRemarks)
admin.site.register(IndividualArrears)
admin.site.register(MaritalStatus)
admin.site.register(PortOfEntry)
admin.site.register(SubsequentPermit)
admin.site.register(SubsequentPermitPayment)
admin.site.register(SubsequentPermitRemarks)
