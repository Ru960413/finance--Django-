# interact with exchange rate currency api
import requests
import urllib.parse
import math


# logic: how much TWD do user need to get the amount of currency they need?
def convert(currency, amount):
    try:
        api_key = 'de854dd1ac96a4c45b041347'
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{urllib.parse.quote_plus(currency)}/TWD/{amount}'
        response = requests.get(url)
        response.raise_for_status()    
    except requests.RequestException:
        return None

    try:
        quote = response.json()
        return {
            "currency":quote["base_code"],
            "rate": quote["conversion_rate"],
            "result": quote["conversion_result"],

        }
    except (KeyError, ValueError, TypeError):
        return None



# for user to query currency rate
def lookup(from_currency, to_currency):
    try:
        api_key = 'de854dd1ac96a4c45b041347'
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{urllib.parse.quote_plus(from_currency)}/{urllib.parse.quote_plus(to_currency)}/1'
        response = requests.get(url)
        response.raise_for_status()    
    except requests.RequestException:
        return None

    try:
        quote = response.json()
        return {
            "currency":quote["base_code"],
            "rate": quote["conversion_rate"],
        }
    except (KeyError, ValueError, TypeError):
        return None


def twd(value):
    return f"{math.ceil(value)}"


