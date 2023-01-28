from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def forward():
    url = 'https://test.tbn.digital'
    forward_response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    headers = dict(forward_response.headers)
    return (forward_response.text, forward_response.status_code, headers)

if __name__ == '__main__':
    app.run(debug=True)
