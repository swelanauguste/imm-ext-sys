from django import forms

from .models import Enquiry, EnquiryRemarks


class EnquiryRemarksCreateForm(forms.ModelForm):
    class Meta:
        model = EnquiryRemarks
        fields = "__all__"
        exclude = ["created_by", "updated_by"]
        widgets = {"enquiry": forms.HiddenInput()}


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
            "time_granted_to": forms.TextInput(attrs={"type": "date"}),
            "validity": forms.TextInput(attrs={"type": "date"}),
        }
