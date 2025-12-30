from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



def welcome(request):
    return render(request, 'welcome.html')

def history(request):
    return render(request, 'history.html')

def important_dates(request):
    return render(request, 'important_dates.html')

def venue(request):
    return render(request, 'venue.html')

def abstract_guidelines(request):
    return render(request, 'abstract_guidelines.html')

def abstract_schedule(request):
    return render(request, 'abstract_schedule.html')

def programme(request):
    return render(request, 'programme.html')

def awards(request):
    return render(request, 'awards.html')

def registration(request):
    return render(request, 'registration.html')

def publication(request):
    return render(request, 'publication.html')

def contact(request):
    return render(request, 'contact.html')

# ----- COMMITTEE PAGES -----
def patrons(request):
    return render(request, 'patrons.html')

def international_committee(request):
    return render(request, 'international_committee.html')

def national_committee(request):
    return render(request, 'national_committee.html')
