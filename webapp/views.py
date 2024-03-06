from django.shortcuts import render
from .webScraping import scrape_clubs

#all of these are how we are connecting from our website to the database through the urls.py

def home(request):
    clubs = Club.objects.all()  # Retrieve all clubs
    return render(request, 'base.html', {'clubs': clubs})

from .models import Club

# this is for the 1st search bar, name of clubs
def club_list(request):
    search_query = request.GET.get('search', '')  # Get the search parameter from the URL
    if search_query:
        clubs = Club.objects.filter(name__icontains=search_query)  # Filter clubs by name
    else:
        clubs = Club.objects.all()  # If no search term is provided, retrieve all clubs
    return render(request, 'base.html', {'clubs': clubs})

#2nd search bar, music type
def music_list(request):
    search_query = request.GET.get('search', '')  # Get the search parameter from the URL
    if search_query:
        clubs = Club.objects.filter(music_type__icontains=search_query)  # Filter clubs by name
    else:
        clubs = Club.objects.all()  # If no search term is provided, retrieve all clubs
    return render(request, 'base.html', {'clubs': clubs})
