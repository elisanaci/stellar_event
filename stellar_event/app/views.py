from urllib import request

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Clients



def view_home(request):
    return render(request,'home.html')
def view_about(request):
    return render(request, 'about_us.html')
def view_packages(request):
    return render(request, 'packages.html')
def view_services(request):
    return render(request, 'services.html')
def view_contact(request):
    return render(request, 'contact.html')



def save_client(request):
    full_name = request.POST['fname']
    email = request.POST['email']
    number = request.POST['number']
    event_type = request.POST['etype']
    event_date = request.POST['edate']
    guest_count = request.POST['guest']
    info = request.POST['info']
    Clients.objects.create(
        full_name=full_name,
        email=email,
        number=number,
        event_type=event_type,
        event_date=event_date,
        guest_count=guest_count,
        info=info,
    )
    messages.success(request, "Thank you for trusting us! We will contact you as soon as possible")
    return redirect('/contact/')



#username:elisa
#email:elisanaci1@gmail.com
#pass:elisan2002
