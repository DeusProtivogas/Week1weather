import requests

# STEP 3: weather for San Francisco
url_SF = "https://wttr.in/san%20francisco?nTqu&lang=en"
response_SF = requests.get(url_SF)
print(response_SF.text)

# STEP 4: weather for London, Sheremetyevo and Cherepovec
url_Lon = "https://wttr.in/london?nTqu&lang=en"
response_Lon = requests.get(url_Lon)
print(response_Lon.text)


url_Sher = "https://wttr.in/~sheremetyevo?nTqu&lang=en"
response_Sher = requests.get(url_Sher)
print(response_Sher.text)


# url_Cher = "https://wttr.in/Cherepovets?nTqu&lang=en"
# response_Cher = requests.get(url_Cher)
# print(response_Cher.text)

# STEP 5: modifications for Cherepovets

url_Cher = "https://wttr.in/Череповец?nTqmM&lang=ru"
response_Cher = requests.get(url_Cher)
print(response_Cher.text)