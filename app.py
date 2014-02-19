from flask import Flask, jsonify
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
        query='share=1').as_string()

    soup = BeautifulSoup(requests.get(url).text)

    question = {}
    question['url'] = url
    question['title'] = soup.find("div", {"class": "question_text_edit"}).text
    question['topics'] = [topic.text for topic in soup.find_all("div", {"class": "topic_list_item"})]
    question['details'] = soup.find("div", {"class": "question_details_text"}).text

    answers = []

    divs = soup.find_all("div", {"class": "pagedlist_item"})
    count = 6 if len(divs) >= 6 else len(divs) - 1
    for i in range(count):
        one_answer = {}
        # TODO: author also has the headline, need to do some regex
        one_answer['author'] = divs[i].find("div", {"class": "answer_user"}).span.text
        one_answer['votes'] = divs[i].find("span", {"class":"numbers"}).text
        # TODO: answer body html
        one_answer['answer'] = divs[i].find("div", {"class": "answer_content"}).text
        one_answer['rank'] = i + 1
        answers.append(one_answer)

    return jsonify(question=question, answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
