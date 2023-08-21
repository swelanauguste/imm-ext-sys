from django.urls import path

from .views import (
    EnquireCreateView,
    EnquiryDetailView,
    EnquiryListView,
    EnquiryRemarksCreateFormView,
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
]
