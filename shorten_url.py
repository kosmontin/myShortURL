import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def is_bitlink(url, token):
    parsed_url = urlparse(url)
    bitlink = ''.join((parsed_url.netloc, parsed_url.path))
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}', headers=headers)
    return True if response.ok else False


def count_clicks(token, url):
    parsed_url = urlparse(url)
    bitlink = ''.join((parsed_url.netloc, parsed_url.path))
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
    params = {'long_url': url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=params)
    response.raise_for_status()
    return response.json()['link']


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    if not token:
        print('Файл .env не найден в текущей папке или в нем отсутствует TOKEN')
        exit()
    url = input('Введите ссылку: ')
    try:
        if is_bitlink(url, token):
            print('По вашей ссылке прошли: {0} раз(а)'.format(count_clicks(token, url)))
        else:
            print('Битлинк: ', shorten_link(token, url))
    except requests.exceptions.HTTPError as e:
        print('Ошибка ввода: \n', e.args)


if __name__ == '__main__':
    main()
