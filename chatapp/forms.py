from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        field_classes = {'username': UsernameField}