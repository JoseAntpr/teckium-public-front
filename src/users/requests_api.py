import requests

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

