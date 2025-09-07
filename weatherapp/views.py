from django.shortcuts import render
import requests
from decouple import config

def weather_data(request):
    weather_data = None
    api_key = config('WEATHERSTACK_API_KEY')

    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
            except requests.RequestException:
                weather_data = {"error": "Unable to fetch weather data"}
            else:
                if "current" in data and "location" in data:
                    current = data["current"]
                    location = data["location"]
                    weather_data = {
                        "city": location.get("name"),
                        "country": location.get("country"),
                        "temperature": current.get("temperature"),
                        "feelslike": current.get("feelslike"),
                        "description": current.get("weather_descriptions", [None])[0],
                        "icon": current.get("weather_icons", [None])[0],
                        "humidity": current.get("humidity"),
                    }
                else:
                    weather_data = {"error": "City not found or invalid response"}

    return render(request, "weatherapp/home.html", {"weather_data": weather_data})
