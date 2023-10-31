from django.contrib import admin

from .models import (
    Enquiry,
    EnquiryPayment,
    EnquiryRemark,
    IndividualArrears,
    MaritalStatus,
    PaymentType,
    PortOfEntry,
    SubsequentPermit,
    SubsequentPermitPayment,
    SubsequentPermitRemark,
)

admin.site.register(Enquiry)
admin.site.register(EnquiryPayment)
admin.site.register(EnquiryRemark)
admin.site.register(IndividualArrears)
admin.site.register(MaritalStatus)
admin.site.register(PortOfEntry)
admin.site.register(SubsequentPermit)
admin.site.register(SubsequentPermitPayment)
admin.site.register(SubsequentPermitRemark)
admin.site.register(PaymentType)
