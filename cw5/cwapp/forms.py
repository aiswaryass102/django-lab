from django import forms
import re

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        
        if email.endswith('@gmail.com'):
            raise forms.ValidationError("Gmail addresses are not allowed")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long")

        return password