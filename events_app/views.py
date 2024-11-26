from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import Event, Participant
from .forms import EventForm, ParticipantForm, ParticipantAccountForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')
def logout(request):
    return render(request, 'logout.html')
def base(request):
    return render(request, 'base.html')

def event(request):
    event=Event.objects.all()
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()  # Save directly to the database
            return render(request, 'event.html', {
                'event_form': EventForm(),  # Reinitialize form
                'message': 'Event added successfully!',
            })
        else:
            return render(request, 'event.html', {
                'event_form': event_form,
                'message': 'Please correct the errors below.',
            })
    else:
        event_form = EventForm()
    return render(request, 'event.html', {'event_form': event_form, 'event': event})
# def event(request):
#     if request.method == 'POST':
#         event_form = EventForm(request.POST)
#         if event_form.is_valid():
#             # new_name=event_form.cleaned_data['name']
#             # new_description=event_form.cleaned_data['description']
#             # new_location=event_form.cleaned_data['location']
#             # new_start_time=event_form.cleaned_data['start_time']
#             # new_end_time=event_form.cleaned_data['end_time']
#             # new_organizer=event_form.cleaned_data['organizer']
#             # new_event=Event(name=new_name,description=new_description,location=new_location,start_time=new_start_time,end_time=new_end_time,organizer=new_organizer)
#             # new_event.save()
#             event_form.save()
#             return render(request, 'event.html', {'event_form': event_form, 'message': 'Event added successfully!'})
#     else:
#         event_form = EventForm()
#     return render(request, 'event.html', {'event_form': event_form})
    
def participant(request):
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)
        if participant_form.is_valid():
            new_name=participant_form.cleaned_data['name']
            new_email=participant_form.cleaned_data['email']
            new_event=participant_form.cleaned_data['event']
            new_participant=Participant(name=new_name,email=new_email,event=new_event)
            new_participant.save()
            # form.save()
            return render(request, 'participant.html', {'participant_form': participant_form, 'message': 'Participant added successfully!'})
    else:
        participant_form = ParticipantForm()
    return render(request, 'participant.html', {'participant_form': participant_form})
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_details.html', {'event': event})
def signup(request):
    if request.method == "POST":
        register_form = ParticipantAccountForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'User registered successfully')
            return redirect('participant')
    else:
        register_form = ParticipantAccountForm()
    return render(request, 'signup.html', {'register_form': register_form})
def login(request):
    if request.method == 'POST':
        login_form = ParticipantAccountForm(request.POST)
        if login_form.is_valid():
            email=login_form.cleaned_data['email']
            password=login_form.cleaned_data['password1']
            myuser = authenticate(username=email, password=password)
        if myuser is not None:
            login(request, myuser)
            return redirect("participant")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "login.html", {'login_form':login_form})
    else:
            login_form=ParticipantAccountForm()
            # messages.error(request, "Invalid username or password")
            # return render(request, "login.html")
    return render(request, "login.html", {'login_form':login_form})
        