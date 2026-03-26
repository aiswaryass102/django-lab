from django import forms

class RegisterForm(forms.Form):
    full_name = forms.CharField(min_length=5, max_length=50)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput
    )