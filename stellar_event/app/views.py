from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def view_contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import Clients, Event

def clients_list(request):
    clients = Clients.objects.all()
    return render(request, 'app/clients_list.html', {'clients': clients})

def event_details(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'app/event_details.html', {'event': event})


def view_home():
    return None