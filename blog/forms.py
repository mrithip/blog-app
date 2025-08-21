from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='name',max_length=100)
    email = forms.EmailField(label="email")
    message = forms.CharField(label='message')