import requests
from django.contrib import messages
from django.shortcuts import redirect

from teckiumDjangoFront.settings import INFO_API


def jwt_required(function):
    def wrap(request, *args, **kwargs):
        token = request.session["jwt"]

        if token:
            token = {'token': token}

            try:
                # Verifica si el token es correcto
                r = requests.post(INFO_API.get("url") + INFO_API.get("version") + "token-verify/", data=token)
                data = r.json()
                if r.status_code == 200 and data.get('token'):
                    print("token-verify: ", r.status_code)
                    print("token-verify: ", data)
                    kwargs['token'] = data['token']
                    kwargs['user'] = data['user']
                    return function(request, *args, **kwargs)
                else:
                    return redirect("/login")
            except requests.exceptions.BaseHTTPError as err:
                print(err)
                messages.warning(request, "El Api no se encuentra disponible")
                return redirect("/login")
            except requests.exceptions.ConnectionError as err:
                print(err)
                messages.warning(request, "El Api no se encuentra disponible")
                return redirect("/login")

        else:
            return redirect("/login")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap