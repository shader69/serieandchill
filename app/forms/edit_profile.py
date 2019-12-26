from django import forms
from django.contrib.auth.forms import UserChangeForm


class MyUserChangeForm(UserChangeForm):
    class Meta:
        # fields = ('username', )
        fields = '__all__'
