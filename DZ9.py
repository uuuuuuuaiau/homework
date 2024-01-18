import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self, currency_code, amount):
        self.currency_code = currency_code
        self.amount = amount
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = 'https://bank.gov.ua/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        usd_rate_element = soup.find('span', {'id': 'usd-rate'})
        usd_rate = float(usd_rate_element.text) if usd_rate_element else None

        return usd_rate

    def convert_to_usd(self):
        if self.usd_rate is not None:
            usd_amount = self.amount / self.usd_rate
            return usd_amount
        else:
            return None

if __name__ == "__main__":
    currency_code = input("Введіть код вашої валюти (наприклад, UAH): ")
    amount = float(input("Введіть суму в вашій валюті: "))

    converter = CurrencyConverter(currency_code, amount)
    usd_amount = converter.convert_to_usd()
