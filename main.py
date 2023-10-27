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

locations = [(url_SF, params_SF), 
             (url_Lon, params_Lon), 
             (url_Sher, params_Sher), 
             (url_Cher, params_Cher)
            ]


def get_weather_forecast(url, params):
        response = requests.get(url, params=params)
        # print(response)
        response.raise_for_status()
        return response.text

def main():
    for loc, params in locations:
        try:
            # print(loc, "  :  ", params)
            result = get_weather_forecast(loc, params)
            # print(result)
            if result is None:
                print (f"Error in URL: {loc}")
            else:
                print (result)
        except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
            print (e) 
        # print ( result.text )

if __name__ == "__main__":
    main()