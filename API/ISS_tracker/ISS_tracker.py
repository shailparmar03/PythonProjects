import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 22.258652
MY_LNG = 71.192383

SERVER = ""
MY_EMAIL = ""
MY_PASS = ""

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        'formatted': 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    ss_data = response.json()
    sunrise = int(ss_data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(ss_data['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    return True if time_now >= sunset or time_now <= sunrise else False


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['latitude'])

    return True if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5 else False


while True:
    if is_iss_overhead() and is_night():
        pass
        connection = smtplib.SMTP(SERVER)
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up \n\nThe ISS is above you in the sky."
        )


