from django import forms

from .models import (
    Enquiry,
    EnquiryPayment,
    EnquiryRemarks,
    SubsequentPermit,
    SubsequentPermitPayment,
)


class EnquiryPaymentCreateForm(forms.ModelForm):
    class Meta:
        model = EnquiryPayment
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "payment_date": forms.TextInput(attrs={"type": "date"}),
        }


class SubsequentPermitPaymentCreateForm(forms.ModelForm):
    class Meta:
        model = SubsequentPermitPayment
        fields = "__all__"
        exclude = ["created_by", "updated_by"]


class SubsequentPermitPaymentUpdateForm(forms.ModelForm):
    class Meta:
        model = SubsequentPermitPayment
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        # widgets = {
        #     "enquiry": forms.HiddenInput(),
        #     "granted_by": forms.HiddenInput(),
        #     "time_granted_from": forms.TextInput(attrs={"type": "date"}),
        #     "time_granted_to": forms.TextInput(attrs={"type": "date"}),
        # }


class SubsequentPermitCreateForm(forms.ModelForm):
    class Meta:
        model = SubsequentPermit
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "enquiry": forms.HiddenInput(),
            "granted_by": forms.HiddenInput(),
            "time_granted_from": forms.TextInput(attrs={"type": "date"}),
            "time_granted_to": forms.TextInput(attrs={"type": "date"}),
        }


class EnquiryRemarksCreateForm(forms.ModelForm):
    class Meta:
        model = EnquiryRemarks
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "enquiry": forms.HiddenInput(),
            "remarks": forms.Textarea(attrs={"rows": 4}),
        }


class EnquiryCreateForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {
            "dob": forms.TextInput(attrs={"type": "date"}),
            "pp_exp": forms.TextInput(attrs={"type": "date"}),
            "pp_issue_date": forms.TextInput(attrs={"type": "date"}),
            "arrival_date": forms.TextInput(attrs={"type": "date"}),
            "time_granted_from": forms.TextInput(attrs={"type": "date"}),
            "time_granted_to": forms.TextInput(
                attrs={"type": "date", "disabled": True}
            ),
            "validity": forms.TextInput(attrs={"type": "date"}),
        }
