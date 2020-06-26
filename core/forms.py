from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control shadow-sm border-0",
            "placeholder": "Name"
        })
    )
    email = forms.EmailField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control shadow-sm border-0",
            "placeholder": "Email"
        })
    )
    phone = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={
            "class": "form-control shadow-sm border-0",
            "placeholder": "Phone"
        })
    )
    subject = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control shadow-sm border-0",
            "placeholder": "Subject"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control shadow-sm border-0",
            "placeholder": "Message"
        })
    )