from django.shortcuts import render
import requests

def home(request):
    city = request.GET.get('city', '')
    weather_data = None
    error_message = None

    if city:
        try:
            geo_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1'
            geo_res = requests.get(geo_url).json()
            if 'results' in geo_res and geo_res['results']:
                lat = geo_res['results'][0]['latitude']
                lon = geo_res['results'][0]['longitude']
                weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
                weather_res = requests.get(weather_url).json()
                weather_data = weather_res.get('current_weather', {})
            else:
                error_message = 'City not found!'
        except Exception as e:
            error_message = 'Error fetching weather data.'

    return render(request, 'index.html', {'weather_data': weather_data, 'city': city, 'error_message': error_message})
#<a href="/" class="btn btn-primary mt-3 px-4">Try another</a>