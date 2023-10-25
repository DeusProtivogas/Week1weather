import requests

url_SF = "https://wttr.in/san%20francisco"
params_SF = {"n": "", 
            "T": "", 
            "u": "", 
            "q": "", 
            "lang": "en",
}

url_Lon = "https://wttr.in/london"
params_Lon = {"n": "", 
              "T": "", 
              "u": "", 
              "q": "", 
              "lang": "en",
            }

url_Sher = "https://wttr.in/svo"
params_Sher = {"n": "", 
              "T": "", 
              "u": "", 
              "q": "", 
              "lang": "en",
              }

url_Cher = "https://wttr.in/Череповец"
params_Cher = {"n": "", 
              "T": "", 
              "M": "", 
              "q": "", 
              "lang": "ru",
}


url_Bad = "https://httpstat.us/"
params_Bad = {"n": "", 
            "T": "", 
            "u": "", 
            "q": "", 
            "lang": "en",
}


locations = [(url_SF, params_SF), 
             (url_Lon, params_Lon), 
             # (url_Bad, params_Bad), 
             (url_Sher, params_Sher), 
             (url_Cher, params_Cher)
            ]

def get_weather_forecast(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
        return None
    return response.text

for loc, params in locations:
    result = get_weather_forecast(loc, params)
    if result is None:
        print("Error in URL: ", loc)
    else:
        print(result)