from django.shortcuts import render, redirect
from .models import Establishment
from .forms import EstablishmentForm
from decouple import config  # Import config to get the environment variable

def home(request):
    return render(request, 'establishments/home.html')

def upload_establishment(request):
    if request.method == 'POST':
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_establishments')
    else:
        form = EstablishmentForm()
    return render(request, 'establishments/upload_establishment.html', {'form': form})

def list_establishments(request):
    establishments = Establishment.objects.all()
    type_filter = request.GET.get('type')
    if type_filter:
        establishments = establishments.filter(type=type_filter)

    mapbox_token = config('MAPBOX_TOKEN')  # Get the Mapbox token from the environment

    return render(request, 'establishments/list_establishment.html', {
        'establishments': establishments,
        'mapbox_token': mapbox_token  # Pass the token to the template
    })
