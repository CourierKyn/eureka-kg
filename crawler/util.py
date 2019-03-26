import requests


def get(url):
    try:
        return requests.get(url, headers={'user-agent': 'my-app/0.0.1'})
    except Exception as e:
        print(e, 'from', url)
