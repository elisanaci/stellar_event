"""
URL configuration for stellar_event project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app import views
from stellar_event import settings
from app.views import view_contact, view_home, view_about, view_services, view_packages, save_client
urlpatterns = [
    path('', view_home),
    path('admin/', admin.site.urls),
    path('home/', view_home),
    path('about_us/', view_about),
    path('contact/', view_contact),
    path('packages/', view_packages),
    path('services/', view_services),
    path('view-save-client/',save_client),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
