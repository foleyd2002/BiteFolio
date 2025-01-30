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
    rating_filter = request.GET.get('rating')
    county_filter = request.GET.get('county')
    sort_order = request.GET.get('sort')

    if type_filter:
        establishments = establishments.filter(type=type_filter)

    if rating_filter:
        establishments = establishments.filter(rating=int(rating_filter))

    if county_filter:
        establishments = establishments.filter(county=county_filter)

    if sort_order == 'asc':
        establishments = establishments.order_by('rating')
    elif sort_order == 'desc':
        establishments = establishments.order_by('-rating')

    mapbox_token = config('MAPBOX_TOKEN')

    return render(request, 'establishments/list_establishment.html', {
        'establishments': establishments,
        'mapbox_token': mapbox_token,
        'counties': Establishment.COUNTIES
    })
