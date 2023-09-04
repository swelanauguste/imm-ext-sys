from allauth.account.forms import SignupForm


class InvitationSignupForm(SignupForm):
    invitation_code = forms.CharField(max_length=20, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["invitation_code"].widget.attrs.update(
            {"placeholder": "Invitation Code"}
        )

    def clean_invitation_code(self):
        # Add your custom validation logic for the invitation code here
        code = self.cleaned_data.get("invitation_code")
        if code != "758":
            raise forms.ValidationError("Invalid invitation code")
        return code
