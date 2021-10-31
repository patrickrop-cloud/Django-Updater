from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import Business, NeighbourHood
from updateme.models import Business

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email', 'user', 'neighbourhood']


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ['name', 'location', 'occupants_count']
