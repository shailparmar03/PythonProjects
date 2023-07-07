from datetime import datetime
import requests

'''------------ISS Location----------'''
# ENDPOINT = "http://api.open-notify.org/iss-now.json"  # for current location
# response = requests.get(url=ENDPOINT)
#
# print(response)  # gives a response code
#
# # 1XX -> Hold on
# # 2XX -> Good to go
# # 3XX -> Yoy don't have permission
# # 4XX -> You Screwed up
# # 5XX -> The server screwed up
#
# # response.raise_for_status()
# data = response.json()
# print(data)

MY_LAT = 22.258652
MY_LNG = 71.192383

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    'formatted': 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params= parameters,)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise,sunset)

time_now = datetime.now()
print(time_now.hour)

