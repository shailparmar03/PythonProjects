from pprint import pprint

import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = 'https://api.sheety.co/3eedbb01362c107b7702a5fc8dea40ac/flightDeals/prices'
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url = self.SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price' :
                    {"iataCode":city['iataCode']}
            }
            response = requests.put(url = f"{self.SHEETY_ENDPOINT}/{city['id']}",json=new_data)
            print(response.text)


if __name__ == '__main__':
    sheet = DataManager()
    data = sheet.get_destination_data()
    pprint(data)
