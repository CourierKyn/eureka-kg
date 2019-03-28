import requests


def get(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6',
    }
    try:
        return requests.get(url, headers=headers)
    except Exception as e:
        print(e, 'from', url)
