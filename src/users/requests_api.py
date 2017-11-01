import requests
from django.conf import settings
from django.core.serializers import json


def tk_authenticate(data):
    '''
    se envian un usuario y contraseña y devuelve un token si está ok
    :param data: json con username y password
    :return: json con token
    '''
    try:
        r = requests.post(settings.INFO_API.get("url") + settings.INFO_API.get("version") + "token-auth/", data=data)
        if not r.status_code == 200:
            return None

        return r.json()
    except ConnectionError:
        return None


def tk_refresh(token):
    try:
        # Refresca el token
        r = requests.post(settings.INFO_API.get("url") + settings.INFO_API.get("version") + "token-refresh/", data=token)
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
        r = requests.post(settings.INFO_API.get("url") + settings.INFO_API.get("version") + "users/", data=data)
        if not r.status_code == 201:
            return None

        return r.json()
    except ConnectionError:
        return None


def get_profile(user_id, token):
    """
    Consulta el API y obtiene los valores del perfil del usuario
    :return: Json recibido
    """
    try:
        r = requests.get(settings.INFO_API.get("url") + settings.INFO_API.get("version") + 'users/' + user_id, headers={'Authorization': 'JWT ' + token})
        if r.status_code == 200:
            configuration = r.json()
            return json.dumps(configuration, indent=4)
        else:
            return None
    except requests.exceptions.ConnectionError:
        return None


def put_profile(user_id, file, json, token):
    """
    Actualiza los valores del perfil del usuario
    :param json: Archivo json con la configuración del recomendador
    :return: None si hay algun problema y el status code si esta ok
    """
    print(user_id)
    print(json)

    try:
        if file.get('profile.avatar'):
            r = requests.put(settings.INFO_API.get("url") + settings.INFO_API.get("version") + "users/" + str(user_id) + "/", files=file, data=json, headers={'Authorization': 'JWT ' + token})
        else:
            r = requests.put(settings.INFO_API.get("url") + settings.INFO_API.get("version") + "users/" + str(user_id) + "/", data=json, headers={'Authorization': 'JWT ' + token})
        if r.status_code == 200:
            return r.status_code
        else:
            return None
    except requests.exceptions.ConnectionError:
        return None