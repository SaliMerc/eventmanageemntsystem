from django import forms
from .models import Event, Participant
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels={
            'name': 'Event Name',
            'description': 'Event Description',
            'location': 'Event Location',
            'start_time': 'Start Time',
            'end_time': 'End Time',
            'organizer': 'Event Organizer',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'organizer': forms.TextInput(attrs={'class': 'form-control'}),
        }
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        labels={
            'name': 'Participant Name',
            'email': 'Participant Email',
            'event':'Event',
        }
            # 'password1': 'Password',
            # 'password2':'Confirm Password',           
            # 'event':'Event',
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
        }
            # 'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'event': forms.Select(attrs={'class': 'form-control'}),
        
class ParticipantAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }