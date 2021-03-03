from django.shortcuts import render
from django.db.models import F
from .models import *


def csc_view(request):
    all = Country.objects.filter(country_name=F('id')).filter(country_name__state_name=F('country_name__id'))
    return render(request, 'index.html', {"all": all})
