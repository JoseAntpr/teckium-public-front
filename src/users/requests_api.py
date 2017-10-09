import requests
from django.contrib import messages

from teckiumDjangoFront.settings import INFO_API, INFO_Client


def tk_authenticate(data):
    '''
    se envian un usuario y contraseña y devuelve un token si está ok
    :param data: json con username y password
    :return: json con token
    '''
    try:
        r = requests.post(INFO_API.get("url") + INFO_API.get("version") + "token-auth/", data=data)
        if not r.status_code == 200:
            return None

        return r.json()
    except ConnectionError:
        return None


def tk_refresh(token):
    try:
        # Refresca el token
        r = requests.post(INFO_API.get("url") + INFO_API.get("version") + "token-refresh/", data=token)
        data = r.json()
        print("token-refresh: ", r.status_code)
        print("token-refresh: ", data)
        if r.status_code == 200:
            return data
        else:
            return None
    except requests.exceptions.BaseHTTPError:
        return None
    except requests.exceptions.ConnectionError:
        return None


def create_user(data):
    '''
    se envian un usuario y contraseña y devuelve un token si está ok
    :param data: json con username y password
    :return: json con token
    '''
    try:
        r = requests.post(INFO_API.get("url") + INFO_API.get("version") + "users/", data=data)
        print(r.status_code)
        print(r.json())
        if not r.status_code == 200:
            return None

        return r.json()
    except ConnectionError:
        return None
