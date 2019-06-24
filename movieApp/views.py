from django.shortcuts import render
from django.contrib import messages
from airtable import Airtable
import os

# Create your views here.


def home_page(request):
    return render(request, 'movieApp/index.html')