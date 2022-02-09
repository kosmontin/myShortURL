import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def count_clicks(token, url):
    bitlink = ''.join((urlparse(url).netloc, urlparse(url).path))
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    params = {'unit': 'month', 'units': -1}
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
        headers=headers,
        params=params
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def shorten_link(token, url):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {'long_url': url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
    response.raise_for_status()
    return 'Битлинк ' + response.json()['link']


def main():
    load_dotenv()
    token = os.getenv('bitly_token')
    if not token:
        print('Файл .env не найден в текущей папке или в нем отсутствует TOKEN')
        exit()
    url = input('Введите ссылку: ')
    try:
        # print(shorten_link(token, url))
        print(count_clicks(token, url))
    except requests.exceptions.HTTPError as e:
        print('Ошибка ввода: \n', e.args)


if __name__ == '__main__':
    main()
