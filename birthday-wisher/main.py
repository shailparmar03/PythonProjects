##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
curr_month = now.month
curr_day = now.day
today=(curr_month,curr_day)

data = pd.read_csv("birthdays.csv")
birthday_dictionary = {(data['month'],data['day']):row for (index,row) in data.iterrows()}

if today in birthday_dictionary:
    birthday_person = birthday_dictionary[today]
    file=f"\letter_templates\letter_{random.choice(1,3)}.txt"
    with open(file) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]',birthday_person['name'])

    with smtplib.SMTP('connection_name') as connection:
        connection.starttls()
        connection.login(EMAIL,PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person['email'],
            msg=f'HAPPY BIRTHDAY\n\n{contents}'
        )





