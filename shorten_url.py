import os
from pprint import pprint

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('bitly_token')
    if not token:
        print('Файл .env не найден в текущей папке или в нем отсутствует TOKEN')
        exit()
    url = input('Введите ссылку: ')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {'long_url': url}
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data).json()
    print(response['link'])


if __name__ == '__main__':
    main()
