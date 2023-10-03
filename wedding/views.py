from django.shortcuts import render
from .forms import Guest_Info
from django import forms


    


# Create your views here.
def index(request):
    return render(request, "wedding/index.html")

def reserve(request):
    rsvps = []
    
    if request.method == 'POST':
        num_rsvps = int(request.POST.get('num_rsvps', 0))
        for _ in range(num_rsvps):
            rsvps.append(Guest_Info(request.POST))

    return render(request, 'wedding/reserve.html', {'rsvps': rsvps})