from django.contrib import admin
from app.models import Clients

admin.site.register(Clients)

# python manage.py createsuperuser