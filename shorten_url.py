import json
import os
from pprint import pprint

import requests
from dotenv import load_dotenv


def main(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get('https://api-ssl.bitly.com/v4/user', headers=headers)
    pprint(json.loads(response.text), sort_dicts=False)


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('bitly_token')
    if token:
        main(token)
    else:
        print('Файл .env не найден в текущей папке или в нем отсутствует TOKEN')
