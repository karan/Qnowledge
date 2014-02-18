from flask import Flask
from bs4 import BeautifulSoup
import requests
from purl import URL

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello!'

@app.route('/url=<path:q_link>')
def get_data(q_link):
    url = URL(q_link)
    if url.domain() not in ['quora.com', 'www.quora.com']:
        return 'error, not quora'

    url = URL(
        scheme='https',
        host='www.quora.com',
        path=url.path(),
        query='share=1')
    return url.as_string()

if __name__ == '__main__':
    app.run(debug=True)
