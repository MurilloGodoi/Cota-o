import requests
import json

class ListValors():

    def __init__(self, currency):
        self._currency = currency

    def request_api(self):
        response = requests.get(
            f'https://economia.awesomeapi.com.br/json/{self._currency}')    

        if response.status_code == 200:
            return response.json()
        else:
            print("Currency not found")
            return response.status_code   
            
    def list_informations(self):
        datas_api = self.request_api()
        print("\n")
        print("Code: " , datas_api[0]['code'])
        print("Name: ",datas_api[0]['name'])
        print("Highest value in the day: ",datas_api[0]['high'])
        print("Lowest value in the day: ",datas_api[0]['low'])
        print("Variation in the day: ",datas_api[0]['varBid'])
        print("\n")
        
currency = input("Enter the name of the currency: ")
currency = ListValors(currency)
currency.list_informations()

