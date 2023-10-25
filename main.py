import requests

url_SF = "https://wttr.in/san%20francisco?nTqu&lang=en"
url_Lon = "https://wttr.in/london?nTqu&lang=en"
url_Sher = "https://wttr.in/~sheremetyevo?nTqu&lang=en"
url_Cher = "https://wttr.in/Череповец?nTqmM&lang=ru"

locations = [url_SF, url_Lon, url_Sher, url_Cher]

def get_weather_forecast(url):
    response = requests.get(url)
    return response.text

for loc in locations:
    print(get_weather_forecast(loc))