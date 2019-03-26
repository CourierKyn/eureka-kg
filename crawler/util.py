import requests


def get(url):
    try:
        return requests.get(url)
    except Exception as e:
        print(e, 'from', url)
