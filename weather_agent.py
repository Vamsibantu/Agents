import requests

def get_weather(city):
    geo_response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }
    )
    geo_data = geo_response.json()

    if "results" not in geo_data:
        return {"error": "City not found"}

    location = geo_data["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]
    weather_response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        }
    )
    return weather_response.json()