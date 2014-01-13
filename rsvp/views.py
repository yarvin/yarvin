from django.shortcuts import render
from django.http import HttpResponse

from rsvp.models import Guest

def index(request):
    return render(request, 'rsvp/form.html')

def thanks(request):
    Guest(name=request.POST['name'],
            attendance=request.POST['attendance'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            zipcode=request.POST['zipcode']).save()
    return render(request, 'rsvp/thanks.html')
