from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display_data(request):
    return render(request, 'generic.html')


