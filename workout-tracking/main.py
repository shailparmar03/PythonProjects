import requests
from datetime import datetime

APP_ID = '5224fefc'
API_KEY ='e5dfe1f3a68970d4af7c9cff19481b33'

GENDER = 'male'
WEIGHT_KG = 55
HEIGHT_CM = 160
AGE = 22

EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT ='https://api.sheety.co/3eedbb01362c107b7702a5fc8dea40ac/workoutTracking/workouts'


headers ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()
exercise = result['exercises'][0]['name']
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']
print(result)
print(exercise,duration,calories)

sheety_headers = {'Authorization': 'Bearer shailstoken123Adbasf124bfu4bf83b1'}
sheety_response = requests.get(url=SHEETY_ENDPOINT,headers=sheety_headers)
sheety_response = sheety_response.json()
print(sheety_response)

today = datetime.today().strftime("%d/%m/%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")



post_data = {
    'workout': {'date': today,
                  'time': current_time,
                  'exercise': exercise.title(),
                  'duration': duration,
                  'calories':calories,
                 }
}

sheety_post_response = requests.post(url=SHEETY_ENDPOINT,json=post_data,headers=sheety_headers)
print(sheety_post_response.text)

