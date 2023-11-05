"""
Подключіться до API НБУ, отримайте теперішній курс валют и запишіть його в TXT-файл в такому форматі:
 "[дата, на яку актуальний курс]"
1. [назва валюти 1] to UAH: [значення курсу валюти 1]
2. [назва валюти 2] to UAH: [значення курсу валюти 2]
3. [назва валюти 3] to UAH: [значення курсу валюти 3]
...
n. [назва валюти n] to UAH: [значення курсу валюти n]
опціонально передбачте для користувача можливість обирати дату, на яку він хоче отримати курс
"""

import requests


class ExchangeRate:
    def __init__(self):
        self.url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        self.data = None
        self.date = None
        self.response = None

    def get_exchange_rate(self):
        try:
            self.response = requests.get(self.url)
        except:
            print('Щось пішло не так!')
        else:
            if 200 <= self.response.status_code < 300:
                self.data = self.response.json()
                self.date = self.data[0]["exchangedate"]


        updated_data = []
        for currency in self.data:
            if currency["cc"] != "RUB":
                updated_data.append(currency)
        self.data = updated_data

    def txt_file(self):
        if not self.data:
            return

        with open("ExchangeRate.txt", "w", encoding="utf-8") as file:
            file.write(f"Дата курсу: {self.date}\n\n")

            counter = 0
            for currency in self.data:
                name = currency["txt"]
                value = currency["rate"]
                counter += 1
                file.write(f"{counter}. {name} на Гривню: {value}\n")

    def end_res(self):
        self.get_exchange_rate()
        self.txt_file()


currency_rate = ExchangeRate()
currency_rate.end_res()
