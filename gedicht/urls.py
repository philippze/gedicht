"""
URL configuration for gedicht project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from cms_gedicht.views import KeinValentinstagsgedichtView, BestellungCreateView

urlpatterns = [
    path('gedicht/', RedirectView.as_view(url='/gedicht/kein-valentinstagsgedicht/')),
    path('gedicht/kein-valentinstagsgedicht/', KeinValentinstagsgedichtView.as_view()),
    path('gedicht/admin/', admin.site.urls),
    path('gedicht/api/bestellung/create/', BestellungCreateView.as_view(), name="bestellung-create"),
]
