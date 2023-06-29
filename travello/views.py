from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Ahmedabad'
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'Sweet Home'
    dest2.price = 800
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Gandhinagar'
    dest3.img = 'destination_3.jpg'
    dest3.desc = 'Little Brother of Chandigadh'
    dest3.price = 650
    dest3.offer = True

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
