from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
        path('welcome-message/', views.welcome, name='welcome'),
    path('aac-history/', views.history, name='history'),
    path('important-dates/', views.important_dates, name='important_dates'),
    path('venue/', views.venue, name='venue'),

    path('abstract-guidelines/', views.abstract_guidelines, name='abstract_guidelines'),
    path('abstract-schedule/', views.abstract_schedule, name='abstract_schedule'),

    path('programme/', views.programme, name='programme'),
    path('awards/', views.awards, name='awards'),
    path('registration/', views.registration, name='registration'),
    path('publication/', views.publication, name='publication'),

    path('contact/', views.contact, name='contact'),

    # COMMITTEE
    path('committee/patrons/', views.patrons, name='patrons'),
    path('committee/international/', views.international_committee, name='international_committee'),
    path('committee/national/', views.national_committee, name='national_committee'),
]
