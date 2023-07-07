import requests
"""PENDING : Trilio account required"""

OPM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = 'c4143793bf115d2ef389b09d067a533f'
MY_LAT = 29.431585
MY_LNG = 106.912254

weather_params = {
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid":api_key,

}

response = requests.get(url=OPM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

weather_id = []

# Next 12 hours (4*3)
weather_slice = weather_data['list'][:4]

will_rain= False

for three_hr_data in weather_slice:
    condition_code = three_hr_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring umbrella")