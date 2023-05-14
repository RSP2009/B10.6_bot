import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class CurceConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://openexchangerates.org/api/latest.json?app_id=a90ee9d5a5d34b4ca52c36d9f0fdaa4b&base={quote_ticker}&symbols={base_ticker}')
        total_base = (json.loads(r.content)[keys[base]])*float(amount)

        return total_base



