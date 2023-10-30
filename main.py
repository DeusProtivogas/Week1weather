import requests
from urllib.parse import urljoin

url_base = "https://wttr.in/"

params_en = {
    "n": "",
    "T": "",
    "u": "",
    "q": "",
    "lang": "en",
}

params_ru = {
    "n": "",
    "T": "",
    "M": "",
    "q": "",
    "lang": "ru",
}

locations = [
    (urljoin(url_base, "san%20francisco"), params_en),
    (urljoin(url_base, "london"), params_en),
    (urljoin(url_base, "svo"), params_en),
    (urljoin(url_base, "Череповец"), params_ru)
]


def get_weather_forecast(url, params):
    response = requests.get(
        url,
        params=params,
    )
    response.raise_for_status()
    return response.text


def main():
    for loc, params in locations:
        try:
            result = get_weather_forecast(loc, params)
            print(result)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError
        ):
            print(f"Error in URL: {loc}")


if __name__ == "__main__":
    main()
