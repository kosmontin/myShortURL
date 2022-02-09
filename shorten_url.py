import os

import requests
from dotenv import load_dotenv


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
        print(shorten_link(token, url))
    except requests.exceptions.HTTPError as e:
        print('Ошибка ввода: \n', e.args)


if __name__ == '__main__':
    main()
