from django.shortcuts import render

# Create your views here.

from shangmen.models import HomeBar


def home_info(request):
    homeBar = HomeBar.objects.all()
    