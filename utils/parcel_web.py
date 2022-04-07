import requests


def check_token(token):
    cookies = {
        'language': 'en',
        'account_token': token,
    }

    params = {
        'caller': 'yes',
        'compression': 'yes',
        'version': '4',
        '_': '1649187939922',
    }

    response = requests.get('https://data.parcelapp.net/data.php', params=params, cookies=cookies)

    return 'VERIFICATIONFAILURE' not in response.text


def fetch_packages(token):
    cookies = {
        'language': 'en',
        'account_token': token,
    }

    params = {
        'caller': 'yes',
        'compression': 'yes',
        'version': '4',
        '_': '1649187939922',
    }

    response = requests.get('https://data.parcelapp.net/data.php', params=params, cookies=cookies)

    return response.json()
