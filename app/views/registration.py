from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from app.forms.create_user import MyUserCreationForm
from app.forms.edit_password import MyPasswordChangeForm
from app.forms.edit_profile import MyUserChangeForm


def create_user(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
        return render(request, 'registration/create_user.html', {'form': form})


def edit_password(request):
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyPasswordChangeForm(request.user)
        return render(request, 'registration/password_change_form.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        form = MyUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your data were successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyUserChangeForm(instance=request.user)
        return render(request, 'registration/edit_profile.html', {'form': form})

