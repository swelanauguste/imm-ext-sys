from django.urls import path

from .views import (
    EnquireCreateView,
    EnquiryDetailView,
    EnquiryListView,
    EnquiryPaymentCreateView,
    EnquiryPaymentDetailView,
    EnquiryRemarksCreateFormView,
    SubsequentPermitCreateView,
    SubsequentPermitDetailView,
)

urlpatterns = [
    path("", EnquiryListView.as_view(), name="enquiry-list"),
    path("create/", EnquireCreateView.as_view(), name="enquiry-create"),
    path("detail/<int:pk>/", EnquiryDetailView.as_view(), name="enquiry-detail"),
    path(
        "enquiry/<int:enquiry_id>/add_comment/",
        EnquiryRemarksCreateFormView.as_view(),
        name="add-enquiry-remark",
    ),
    path(
        "subsequent-permit/create/<int:enquiry_id>/",
        SubsequentPermitCreateView.as_view(),
        name="subsequent-permit-create",
    ),
    path(
        "subsequent-permit/detail/<int:pk>/",
        SubsequentPermitDetailView.as_view(),
        name="subsequent-permit-detail",
    ),
    path(
        "enquiry-payment/create/<int:pk>/",
        EnquiryPaymentCreateView.as_view(),
        name="enquiry-payment-create",
    ),
    path(
        "enquiry-payment/detail/<int:pk>/",
        EnquiryPaymentDetailView.as_view(),
        name="enquiry-payment-detail",
    ),
]
