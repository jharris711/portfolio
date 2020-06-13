from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name"
        })
    )
    email = forms.EmailField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Email"
        })
    )
    phone = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Phone"
        })
    )
    subject = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Message"
        })
    )