import os
import random

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def insta_proxy():
    insta_url = request.query_string.decode('utf-8').replace('url=', '')
    if insta_url is None or insta_url == '':
        return 'Media url is not provided', 400

    available_proxies = list(os.environ.get('PROXIES', '').split(','))
    if available_proxies:
        proxies = {'https': random.choice(available_proxies)}
    else:
        proxies = {}
    try:
        response = requests.get(insta_url, stream=True, proxies=proxies)
    except Exception as e:
        return str(e), 400
    response.headers.pop('cross-origin-resource-policy', None)
    return response.content, response.status_code, response.headers.items()


if __name__ == '__main__':
    app.run()
