from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class MyPasswordChangeForm(PasswordChangeForm):
    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2', )
