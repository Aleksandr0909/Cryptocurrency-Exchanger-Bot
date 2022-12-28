import requests
import config


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.EXCHANGE_API_KEY,
}
session = requests.Session()
session.headers.update(headers)


def get_price(currency: str, convert_to: str) -> float:
    parameters = {
        'convert': convert_to,
        'symbol': currency,
    }

    try:
        response = session.get(url, params=parameters)
    except (ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
        print(e)

    if not response.ok:
        raise ValueError('Неправильный ответ от сервера!')

    data = response.json()
    return data['data'][currency]['quote'][convert_to]['price']
