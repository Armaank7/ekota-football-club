from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StaffRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    # the other fields like username, password1 and password2 are already created by default in django user, these are extra fields.

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
