import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def insta_proxy():
    insta_url = request.query_string.decode('utf-8').replace('url=', '')
    response = requests.get(insta_url, stream=True)
    response.headers.pop('cross-origin-resource-policy')
    return response.content, response.status_code, response.headers.items()


if __name__ == '__main__':
    app.run()
