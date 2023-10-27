import requests

url_base = "https://wttr.in/"

params_en = {"n": "", 
            "T": "", 
            "u": "", 
            "q": "", 
            "lang": "en",
}

params_ru = {"n": "", 
              "T": "", 
              "M": "", 
              "q": "", 
              "lang": "ru",
}


def get_url(location):
    return url_base + location

locations = [(get_url("san%20francisco"), params_en), 
             (get_url("london"),params_en), 
             (get_url("svo"), params_en), 
             (get_url("Череповец"), params_ru)
            ]


def get_weather_forecast(url, params):
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text

def main():
    for loc, params in locations:
        try:
            result = get_weather_forecast(loc, params)
            if result is None:
                print (f"Error in URL: {loc}")
            else:
                print (result)
        except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
            print (e) 

if __name__ == "__main__":
    main()