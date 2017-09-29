import requests


API_URL = "http://127.0.0.1:8001/api/"
version = "1.0/"


def tk_authenticate(data):
    '''
    se envian un usuario y contraseña y devuelve un token si está ok
    :param data: json con username y password
    :return: json con token
    '''
    r = requests.post(API_URL+version+"auth/", data=data)

    if not r.status_code == 200:
        return None

    return r.json()
