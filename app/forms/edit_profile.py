from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email')
