import requests

from teckiumDjangoFront.settings import INFO_API, INFO_Client


def get_posts(filters, *argv):
    '''
    Se envian los filtros a la llamada al API status=2
    :param filters: json con los params
    :return: json con los posts
    '''
    try:
        r = requests.get(INFO_API.get("url") + INFO_API.get("version") + 
                         "posts/", params=filters)

        if not r.status_code == 200:
            return None

        return r.json()
    except ConnectionError:
        return None

def get_post(post_pk):
    '''
    Se envian los filtros a la llamada al API status=2
    :param filters: json con los params
    :return: json con los posts
    '''
    try:
        r = requests.get(INFO_API.get("url") + INFO_API.get("version") + "posts/" + post_pk + "/")

        if not r.status_code == 200:
            return None

        return r.json()
    except ConnectionError:
        return None

def get_comments(filters):
    try:
        r = requests.get(INFO_API.get("url") + INFO_API.get("version") + 
                         "comments/", params=filters)
        if not r.status_code == 200:
            return None
        
        return r.json()
    except ConnectionError:
        return None


def get_tags(*argv):

    try:
        r = requests.get(INFO_API.get("url") + INFO_API.get("version") + "tags/") if not argv else requests.get(
            INFO_API.get("url") + INFO_API.get("version") + "tags/" + argv[0] + "/")
        if not r.status_code == 200:
            return None

        return r.json()
    except ConnectionError:
        return None
